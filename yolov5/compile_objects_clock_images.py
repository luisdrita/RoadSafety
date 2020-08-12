import os
import pandas as pd
import json

lsoa_objects_number = {}

data = pd.read_csv (r'./image_labels.csv')



df1 = pd.DataFrame(data, columns= ['img_id'])

imgId2lsoa = {}

data = pd.read_csv (r'image_labels.csv')

img_ids_clock = []

for i in range(0, data['img_id'].size):

    imgId2lsoa[str(data['img_id'][i])] = data['lsoa11'][i]

for root, dirs, files in os.walk("./yolov5/results"):
    for filename in files:
        file1 = open('./yolov5/results/' + filename, 'r')
        Lines = file1.readlines()

        for line in Lines:       

            if line.strip().split(" ")[0] == "74":

                img_ids_clock.append(filename)
                
outF = open("img_ids_clock.txt", "w")
for line in img_ids_clock:
  # write line to output file
  outF.write(line)
  outF.write("\n")
outF.close()