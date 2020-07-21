import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

from model import PSPNet101, PSPNet50
from tools import *
import imageio
import pandas as pd
import os
import time
import sys
# import numpy
# from numpy import savetxt

# ------------------------------------------

def pre_process(I, h, w):
    J = np.concatenate([I[:, :, 2][:, :, None], I[:, :, 1][:, :, None], I[:, :, 0][:, :, None]], axis=2)
    J = J.astype(np.float32) - IMG_MEAN
    h_, w_ = np.max([h, I.shape[0]]), np.max([w, I.shape[1]])
    K = np.zeros((h_, w_, 3), dtype=np.float32)
    K[:I.shape[0], :I.shape[1], :] = J
    return K


def post_process(preds, outputs, I):
    return preds[:, :I.shape[0], :I.shape[1], :], outputs[:, :I.shape[0], :I.shape[1]]


def pspnet_segmentation(img, angle):

    print(rds_path + 'images/{}_{}.png'.format(img, angle))

    seg_path = save_dir + '{}_{}_segmentation.png'.format(img, angle)
    img_path = rds_path + '../london-images-new/{}_{}.png'.format(img, angle)
    
    if os.path.exists(img_path):

        if not os.path.exists(seg_path):
            print('processing {}'.format(img_path))

            I_ = imageio.imread(img_path)
            J_ = pre_process(I_, crop_size[0], crop_size[1])

            preds, outputs = sess.run([pred, raw_output_up], feed_dict={I: J_[None, :, :, :]})
            preds, outputs = post_process(preds, outputs, I_)

            # print(preds)
            # print("--------------------------------------")
            # print(outputs)
            # print("--------------------------------------")
            
            # savetxt(seg_path.split(".")[0] + ".csv", outputs[0], delimiter=',')
            
            imageio.imwrite(seg_path, preds[0].astype(np.uint8))

        else:

            print('already processeed {}'.format(img_path))
    
def load(saver, sess, ckpt_path):

    saver.restore(sess, ckpt_path)
    print("Restored model parameters from {}".format(ckpt_path))

# ------------------------------------------ CONSTANTS

rds_path = '/rds/general/user/lr3118/home/pspnet101/'  # path to rds project location or hpc personal space etc.
save_dir = '/rds/general/user/lr3118/home/pspnet101/results/segmented_imgs_lsoa/'  # directory for saving segmentation outputs

IMG_MEAN = np.array((103.939, 116.779, 123.68), dtype=np.float32)

cityscapes_param = {'crop_size': [720, 720],
                    'num_classes': 19,
                    'model': PSPNet101}

## CHOSE WHICH TRAINED NETWORK YOU WANT TO USE
dataset = 'cityscapes'  # >> tree id is 8
flipped_eval = True

# load parameters
# you need to get the parameters stored here https://github.com/hellochick/PSPNet-tensorflow

param = cityscapes_param
checkpoints = rds_path + 'model/cityscapes/'

crop_size = param['crop_size']
num_classes = param['num_classes']
PSPNet = param['model']
img_size = (640, 640)

h, w = np.max([img_size[0], crop_size[0]]), np.max([img_size[1], crop_size[1]])

# ---------



# ---------

# d = {'img_id': [["111"], ["111"], ["111"], ["111"], ["221"], ["221"], ["221"], ["221"]]}
# df = pd.DataFrame(data=d)

# data = pd.read_csv (r'../image_labels.csv')

# df = pd.DataFrame(data, columns= ['img_id'])

# print(df.size)

# df_split = np.array_split(df, 24)

# l = []

# for k in range(24): 

    # l.append(df_split[k])

# ------------------------------------------

# Create network.
I = tf.placeholder(tf.float32, shape=(None, h, w, 3))
net = PSPNet({'data': I}, is_training=False, num_classes=num_classes)

with tf.variable_scope('', reuse=True):
    flipped_img = tf.image.flip_left_right(tf.squeeze(I))
    flipped_img = tf.expand_dims(flipped_img, dim=0)
    net2 = PSPNet({'data': flipped_img}, is_training=False, num_classes=num_classes)

raw_output = net.layers['conv6']

# Do flipped eval or not
flipped_output = tf.image.flip_left_right(tf.squeeze(net2.layers['conv6']))
flipped_output = tf.expand_dims(flipped_output, dim=0)
raw_output = tf.add_n([raw_output, flipped_output])

# Predictions.
raw_output_up = tf.image.resize_bilinear(raw_output, size=[h, w], align_corners=True)
# raw_output_up = tf.image.crop_to_bounding_box(raw_output_up, 0, 0, img_shape[0], img_shape[1])
raw_output_up = tf.argmax(raw_output_up, axis=3)
pred = decode_labels(raw_output_up, [h, w], num_classes)

# Init tf Session
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
init = tf.global_variables_initializer()

sess.run(init)

restore_var = tf.global_variables()

ckpt = tf.train.get_checkpoint_state(checkpoints)
# print(checkpoints)
# print(ckpt)

if ckpt and ckpt.model_checkpoint_path:
    loader = tf.train.Saver(var_list=restore_var)
    load_step = int(os.path.basename(ckpt.model_checkpoint_path).split('-')[1])
    load(loader, sess, ckpt.model_checkpoint_path)
else:
    print('No checkpoint file found.')

'''
    
sindex = int(sys.argv[1])
start_index = 10000*(sindex-1)
end_index = 10000*(sindex)
# split the dataframe into smaller dataframes and call the segmentation function
df = df['img_id'][start_index:end_index]

startTime=time.time()

'''

right_files = []

with open('../select_lsoa/list_images.txt') as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        right_files.append((line.split("\n")[0]).split(".")[0] + ".png")
        
# print(right_files)

for img_array_it in right_files:       

    pspnet_segmentation(img_array_it.split("_")[0], "a")

