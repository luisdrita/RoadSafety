from shutil import copyfile
import os

right_files = []
all_files = []

with open('../imagery_dataset/one_img_per_lsoa.txt') as fp:
    line = fp.readline()
    while line:
        line = fp.readline()
        right_files.append((line.split("\n")[0]).split(".")[0])

for root, dirs, files in os.walk("yolofinal"):
    for filename in files:
        all_files.append(filename)

for file in right_files:
    for filename in all_files:
        if filename == file:
            copyfile("yolofinal/" + filename, "yolofinal/yolofinal_lsoa/" + filename)