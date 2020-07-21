from __future__ import print_function

# import time
# import datetime
# import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

from model import PSPNet101, PSPNet50
from tools import *

import imageio
import pandas as pd

import multiprocessing

import os
import datetime

tf.reset_default_graph()

rds_path = '/rds/general/user/lr3118/home/esra/'  # path to rds project location or hpc personal space etc.

IMG_MEAN = np.array((103.939, 116.779, 123.68), dtype=np.float32)

ADE20k_param = {'crop_size': [473, 473],
                'num_classes': 150,
                'model': PSPNet50}

cityscapes_param = {'crop_size': [720, 720],
                    'num_classes': 19,
                    'model': PSPNet101}


def pre_process(I, h, w):
    J = np.concatenate([I[:, :, 2][:, :, None], I[:, :, 1][:, :, None], I[:, :, 0][:, :, None]], axis=2)
    J = J.astype(np.float32) - IMG_MEAN
    h_, w_ = np.max([h, I.shape[0]]), np.max([w, I.shape[1]])
    K = np.zeros((h_, w_, 3), dtype=np.float32)
    K[:I.shape[0], :I.shape[1], :] = J
    return K


def post_process(preds, outputs, I):
    return preds[:, :I.shape[0], :I.shape[1], :], outputs[:, :I.shape[0], :I.shape[1]]


def pspnet_segmentation(df):
    for img in df['img_id'][0:10]:
        for hid in ['a', 'b', 'c', 'd']:
            print(rds_path + 'images/{}_{}.png'.format(img, hid))
            seg_path = save_dir + '{}_{}_segmentation.png'.format(img, hid)
            img_path = rds_path + 'images/{}_{}.png'.format(img, hid)
            if not os.path.exists(seg_path):
                print('processing {}'.format(img_path))

                I_ = imageio.imread(img_path)
                J_ = pre_process(I_, crop_size[0], crop_size[1])

                preds, outputs = sess.run([pred, raw_output_up], feed_dict={I: J_[None, :, :, :]})
                preds, outputs = post_process(preds, outputs, I_)

                imageio.imwrite(seg_path, preds[0].astype(np.uint8))

            else:

                print('already processeed {}'.format(img_path))

def load(saver, sess, ckpt_path):

    saver.restore(sess, ckpt_path)
    print("Restored model parameters from {}".format(ckpt_path))


## CHOSE WHICH TRAINED NETWORK YOU WANT TO USE
#dataset = 'ade20k'
dataset = 'cityscapes'  # >> tree id is 8
flipped_eval = True

# load parameters
# you need to get the parameters stored here https://github.com/hellochick/PSPNet-tensorflow
if dataset == 'ade20k':
    param = ADE20k_param
    checkpoints = rds_path + 'model/ade20k/'
elif dataset == 'cityscapes':
    param = cityscapes_param
    checkpoints = rds_path + 'model/cityscapes/'

crop_size = param['crop_size']
num_classes = param['num_classes']
PSPNet = param['model']
img_size = (640, 640)

h, w = np.max([img_size[0], crop_size[0]]), np.max([img_size[1], crop_size[1]])

# Create network.
I = tf.placeholder(tf.float32, shape=(None, h, w, 3))
net = PSPNet({'data': I}, is_training=False, num_classes=num_classes)

with tf.variable_scope('', reuse=True):
    flipped_img = tf.image.flip_left_right(tf.squeeze(I))
    flipped_img = tf.expand_dims(flipped_img, dim=0)
    net2 = PSPNet({'data': flipped_img}, is_training=False, num_classes=num_classes)

raw_output = net.layers['conv6']

# Do flipped eval or not
if flipped_eval:
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
print(checkpoints)
print(ckpt)
if ckpt and ckpt.model_checkpoint_path:
    loader = tf.train.Saver(var_list=restore_var)
    load_step = int(os.path.basename(ckpt.model_checkpoint_path).split('-')[1])
    load(loader, sess, ckpt.model_checkpoint_path)
else:
    print('No checkpoint file found.')

# ofile_p = DIR_UPDATE # to update metadata and check to see which images are completed for segmentation
# df = pd.read_pickle(METADATA_PATH) # metadata path for list of images/image paths etc.

save_dir = '/rds/general/user/lr3118/home/esra/segmented_imgs/'  # directory for saving segmentation outputs

d = {'img_id': ["111", "221"]}
df = pd.DataFrame(data=d)

startTime = datetime.now()

pspnet_segmentation(df)

print('It took: ', datetime.now() - startTime)
