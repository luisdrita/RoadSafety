from shutil import copyfile
import os

right_files = []
all_files = []

with open('../list_images.txt') as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        right_files.append((line.split("\n")[0]).split(".")[0] + ".png")

for root, dirs, files in os.walk("london-images-new"):
    for filename in files:
        all_files.append(filename)

for file in right_files:
    for filename in all_files:
        if filename == file:
            copyfile("london-images-new/" + filename, "london-images-new/london-images-new-lsoa/" + filename)