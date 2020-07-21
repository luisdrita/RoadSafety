# pixel-color-count.py - Gets a sum of pixels per unique color
# maintainer - Ashley Grenon @townsean
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

    args = parser.parse_args()

    with Image.open(args.image) as image:
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


if __name__ == '__main__':
    main()