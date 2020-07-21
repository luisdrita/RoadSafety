# pixel-color-count.py - Gets a sum of pixels per unique color
# maintainer - Ashley Grenon @townsean

import pandas as pd

try:
    from PIL import Image

except ImportError:
    exit("This script requires the PIL module. Install with pip install Pillow")

try:
    import webcolors

except ImportError:
    # https://pypi.org/project/webcolors/
    exit("This script uses webcolors for displaying named colors. Install with pip install webcolors")

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
                    color_count[rgb] += 1
                else:
                    color_count[rgb] = 1
		    
print(color_count)
 
data = pd.read_csv (r'../image_labels.csv')

df = pd.DataFrame(data, columns= ['img_id'])

df = df['img_id'][0:10]

for img_array_it in df:

    for angle in ["a", "b", "c", "d"]:

        main("./results/" + str(img_array_it) + '_' + angle + '_' + 'segmentation.png')
