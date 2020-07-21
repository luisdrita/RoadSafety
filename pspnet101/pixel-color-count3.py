# pixel-color-count.py - Gets a sum of pixels per unique color
# maintainer - Ashley Grenon @townsean

import pandas as pd
import json
import time
import imageio

try:
    from PIL import Image

except ImportError:
    exit("This script requires the PIL module. Install with pip install Pillow")

try:
    import webcolors

except ImportError:
    # https://pypi.org/project/webcolors/
    exit("This script uses webcolors for displaying named colors. Install with pip install webcolors")
    

'''
def main(image):

    with Image.open(image) as image:
        color_count = {}
        width, height = image.size
        rgb_image = image.convert('RGB')

        # iterate through each pixel in the image and keep a count per unique color
        for x in range(width):
            for y in range(height):
                rgb = rgb_image.getpixel((x, y))

                if rgb in color_count:
                    color_count[str(rgb)] += 1
                    
                else:
                    color_count[str(rgb)] = 1

    return color_count
'''

def main(image):
      
    im = imageio.imread('imageio:astronaut.png')
    
    print(im[])

data = pd.read_csv (r'../image_labels.csv')

df = pd.DataFrame(data, columns= ['img_id'])

df = df['img_id'][0:10]

all_images_json = {}

startTime=time.time()

for img_array_it in df:

    for angle in ["a", "b", "c", "d"]:

        all_images_json[str(img_array_it) + '_' + angle] = main("./results/" + str(img_array_it) + '_' + angle + '_' + 'segmentation.png')
        
print(startTime - time.time())

print(all_images_json)

# json.dumps(all_images_json)

# json_object = json.dumps(all_images_json)

# with open("all_images_json.json", "w") as outfile:

#    outfile.write(all_images_json)

with open('all_images_json.txt', 'w') as outfile:
    json.dump(all_images_json, outfile)