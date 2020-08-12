import os
import pandas as pd
import json

lsoa_objects_number = {}

data = pd.read_csv (r'./image_labels.csv')

df1 = pd.DataFrame(data, columns= ['img_id'])

imgId2lsoa = {}

data = pd.read_csv (r'image_labels.csv')

for i in range(0, data['img_id'].size):

    imgId2lsoa[data['img_id'][i]] = data['lsoa11'][i]

for root, dirs, files in os.walk("./yolov5/results"):
    for filename in files:
        file1 = open('./yolov5/results/' + filename, 'r')
        Lines = file1.readlines()

        if int(filename.split("_")[0]) in imgId2lsoa and imgId2lsoa[int(filename.split("_")[0])] not in lsoa_objects_number:

            lsoa_objects_number[imgId2lsoa[int(filename.split("_")[0])]] = {}
            
        if int(filename.split("_")[0]) in imgId2lsoa:

            for line in Lines:

                if line.strip().split(" ")[0] not in lsoa_objects_number[imgId2lsoa[int(filename.split("_")[0])]]:

                    lsoa_objects_number[imgId2lsoa[int(filename.split("_")[0])]][line.strip().split(" ")[0]] = 0

                lsoa_objects_number[imgId2lsoa[int(filename.split("_")[0])]][line.strip().split(" ")[0]] = lsoa_objects_number[imgId2lsoa[int(filename.split("_")[0])]][line.strip().split(" ")[0]] + 1
            

with open('lsoa_objects_number.json', 'w') as fp:
    
    json.dump(lsoa_objects_number, fp)