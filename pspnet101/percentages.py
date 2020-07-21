# COLORS MAT TO BE REPLACED WITH CITYSCAPES COLORSMAP
# colors = sio.loadmat(rds_path + 'code/pspnet-outputs/utils/color150.mat')

# color_table = colors['colors']

import pandas as pd
import imageio

seg_dir = "./results/"

data = pd.read_csv (r'../image_labels.csv')
df = pd.DataFrame(data, columns= ['img_id'])

print(df[0:10])

print(imageio.imread(seg_dir + '1_a_segmentation.png'))

print(imageio.imread(seg_dir + '1_a_segmentation.png').shape)

image_color_area = {}

'''

def get_perc(df):
    
    b = 640*640*4
    
    for img_array_it in df:
        
        for angle in ["a", "b", "c", "d"]:
            
            px = 0
            seg_path = seg_dir + '{}_{}_segmentation.png'.format(img, hid)
            
            if os.path.exists(seg_path):
                
                try:
	                    I_ = imageio.imread(seg_path)
	                    px = px + np.sum((I_[:,:,0]==c[0]) & (I_[:,:,1]==c[1]) & (I_[:,:,2]==c[2]))
	                    df.loc[index, 'perc_{}'.format(a)] = px/b
	                except:
	                	print('problem reading image: ', seg_path)
                else:
                	print('path does not exist: ', seg_path)
            
    
    for index, row in df.iterrows():
        img = row['imgid']
        a = 1
        for c in color_table:
            px = 0
            for hid in ['a','b','c','d']:
                seg_path = seg_dir + '{}_{}_segmentation.png'.format(img, hid)
                if os.path.exists(seg_path):
                	try:
	                    I_ = imageio.imread(seg_path)
	                    px = px + np.sum((I_[:,:,0]==c[0]) & (I_[:,:,1]==c[1]) & (I_[:,:,2]==c[2]))
	                    df.loc[index, 'perc_{}'.format(a)] = px/b
	                except:
	                	print('problem reading image: ', seg_path)
                else:
                	print('path does not exist: ', seg_path)
            a = 1 + a
            #print(a)
            
    return df
    
'''

import argparse

try:
    from PIL import Image
except ImportError:
    exit("This script requires the PIL module. Install with pip install Pillow")

try:
    import webcolors
except ImportError:
    # https://pypi.org/project/webcolors/
    exit("This script uses webcolors for displaying named colors. Install with pip install webcolors")

def main():
    parser = argparse.ArgumentParser(description='Calculates the sum of pixels per a color')
    parser.add_argument('image', nargs='?', default='.', help='The image to sum the pixels per a color of')
    # parser.add_argument('-i', '--ignore-color', type=tuple, help='Skip counting pixels of this color')

    imag

    with Image.open(image) as image:
        color_count = {}
        width, height = image.size
        rgb_image = image.convert('RGB')

        # iterate through each pixel in the image and keep a count per unique color
        for x in range(width):
            for y in range(height):
                rgb = rgb_image.getpixel((x, y))

                if rgb in color_count:
                    color_count[rgb] += 1
                else:
                    color_count[rgb] = 1
                    
        print('Pixel Count per Unique Color:')
        print('-' * 30)
        color_index = 1
        for color, count in color_count.items():
            # if color == args.ignore-color:
            #    pass

            try:
                print('{}.) {}: {}'.format(color_index, webcolors.rgb_to_name(color), count))
            except ValueError:                
                print('{}.) {}: {}'.format(color_index, color, count))
            color_index += 1
