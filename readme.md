# Road Safety for Cyclists in London
[Jupyter Notebook](https://github.com/warcraft12321/RoadSafety/blob/master/RoadSafety.ipynb) | [Report](https://github.com/warcraft12321/RoadSafety/blob/master/text/report.pdf) | [Presentation](https://github.com/warcraft12321/RoadSafety/blob/master/text/presentation.pdf)

### Aim

The aim of this project was to use imagery to estimate safety on the roads of London, from a cyclist’s perspective. After
a brief introduction to the most important road safety indicators, a ranked list with several risk factors was compiled.
Risk factors were obtained from Google StreetView (GSV) imagery dataset using the object detection YOLOv5 (released in June 2020 by Glenn Jocher) and
image segmentation PSPNet101 (Pyramid Scene Parsing Network) (released in July 2017 by Hengshuang Zhao et al.).

Imagery dataset contains 518 350 images of greater London, distributed across 4833 boroughs. Each image is labeled in accordance
to the LSOA it belongs. Images are organized in sets of 4 which corresponds to 4 90º angles from a total of 129 588 points.

Both YOLOv5 and PSPNet101 were benchmarked and validated using a set of 1 image per LSOA from the dataset.

Data was storaged and processed in the secure High Performance Cluster from Imperial College London.

### GSV Dataset
#### Stats

![](./img/dataset/number images.png)

Minimum | Maximum | Mean | Standard Deviation | Mode | Median
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
1 | 211 | 27 | 24 | 25 | 11

### Object Detection

YOLOv5 is the most recent version of YOLO which was originally developed by Joseph Redmon. First version runs in framework
called Darknet which was purposely built to execute YOLO.

Version 5 is the 2nd model which was not developed by Joseph Redmon (after version 4) and the first running in the
state-of-the-art machine learning framework PyTorch.

This model was pre-trained using Coco dataset. Thus, it is able to identify 80 object categories. Distributed
over 11 categories.

<details>
  <summary>COCO Categories</summary>

Person | Vehicle | Outdoor | Animal | Accessory | Sports | Kitchen | Food | Furniture | Electronic | Appliance | Indoor
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
Person | Bicycle | Traffic Light | Bird | Backpack | Frisbee | Bottle | Banana | Chair | TV | Microwave | Book
|  | Car | Fire Hydrant | Cat | Umbrella | Skis | Wine Glass | Apple | Couch | Laptop | Oven | Clock
|  | Motorcycle | Stop Sign | Dog | Handbag | Snowboard | Cup | Sandwich | Potted Plant | Mouse | Toaster | Vase
|  | Airplane | Parking Meter | Horse | Tie | Sports Ball | Fork | Orange | Bed | Remote | Sink | Scissors
|  | Bus | Bench | Sheep | Suitcase | Kite | Knife | Broccoli | Dinning Table | Keyboard | Refrigerator | Teddy Bear
|  | Train |  | Cow |  | Baseball Bat | Spoon | Carrot | Toilet | Cell Phone | | Hair Drier
|  | Truck |  | Elephant |  | Baseball Glove | Bowl | Hot dog | | | | Toothbrush
|  | Boat |  | Bear |  | Skateboard | | Pizza | | | |
|  |  |  | Zebra |  | Surfboard | | Donut | | | |
|  |  |  | Giraffe |  | Tennis Racket | | Cake | | | |
|  |  |  |  |  |  | | | | | |
|  |  |  |  |  |  |  | | | | |
|  |  |  |  |  |  |  | | | | |
|  |  |  |  |  |  |  | | | | |
|  |  |  |  |  |  |  | | | | |
|  |  |  |  |  |  |  | | | | |
|  |  |  |  |  |  |  | | | | |


</details>

Original            |  YOLOv5
:-------------------------:|:-------------------------:
![](./img/yolov5/23963_a.png)  |  ![](./img/yolov5/23963_a_processed.png)

[(Click to See 1 Image per LSOA)](https://drive.google.com/drive/folders/1G-EdZtO3bqRzG-OqnumDWjP08yihJ05q?usp=sharing)

#### Stats

![](./img/yolov5/stats.png)

Object            |  Number Occurrences | Object            |  Number Occurrences | Object            |  Number Occurrences
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
Car  |  1509344 | Bicycle  |  10894 | Chair  |  2191
Person  |  107266 | Motorcycle  |  8970 | Handbag  |  2090
Truck  |  70083 | Traffic Light  |  6310 | Backpack  |  1939
Potted Plant  |  37917 | Bench  |  5013 | Stop Sign  |  1282
Bus  |  11512 | Clock  |  2750 | Fire Hydrant  |  1168

Bicycle            |  Bus
:-------------------------:|:-------------------------:
![](./img/yolov5/lsoas/bicycle.png)  |  ![](./img/yolov5/lsoas/bus.png)

Car | Motorcycle
:-------------------------:|:-------------------------:
![](./img/yolov5/lsoas/car.png)  |  ![](./img/yolov5/lsoas/motorcycle.png)

Stop Sign | Traffic Light
:-------------------------:|:-------------------------:
![](./img/yolov5/lsoas/stop sign.png)  |  ![](./img/yolov5/lsoas/traffic light.png)

Truck |
:-------------------------:|:-------------------------:
![](./img/yolov5/lsoas/truck.png)  |


<details>
  <summary>COCO Objects Stats</summary>

Category | Number Occurrences | Minimum | Maximum | Mean
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
Person | 107266 | TBD | TBD | TBD
Bicycle | 10894 | 0 | 144 | 2
Car | 1509344 | 13 | 1891 | 312
Motorcycle | 8970 | 0 | 74 | 1
Airplane | 234 | 0 | 4 | 0
Bus | 11512 | 0 | 36 | 2
Train | 657 | 0 | 5 | 0
Truck | 70083 | 0 | 192 | 14
Boat | 971 | 0 | 22 | 0
Traffic Light | 6310 | 0 | 54 | 1
Fire Hydrant | 1168 | 0 | 11 | 0
Stop Sign | 1282 | 0 | 8 | 0
Parking Meter | 968 | 0 | 7 | 0
Bench | 5013 | 0 | 23 | 1
Bird | 509 | 0 | 9 | 0
Cat | 27 | 0 | 2 | 0
Dog | 419 | 0 | 3 | 0
Horse | 35 | 0 | 2 | 0
Sheep | 13 | 0 | 5 | 0
Cow | 79 | 0 | 2 | 0
Elephant | 2 | 0 | 1 | 0
Bear | 3 | 0 | 1 | 0
Zebra | 5 | 0 | 1 | 0
Giraffe | 22 | 0 | 1 | 0
Backpack | 1939 | 0 | 20 | 0
Umbrella | 378 | 0 | 9 | 0
Handbag | 2090 | 0 | 28 | 0
Tie | 39 | 0 | 5 | 0
Suitcase | 467 | 0 | 8 | 0
Frisbee | 384 | 0 | 4 | 0
Skis | 2 | 0 | 1 | 0
Snowboard | 0 | 0 | 0 | 0
Sports Ball | 102 | 0 | 4 | 0
Kite | 465 | 0 | 16 | 0
Baseball Bat | 7 | 0 | 3 | 0
Baseball Glove | 1 | 0 | 1 | 0
Skateboard | 245 | 0 | 3 | 0
Surfboard | 80 | 0 | 2 | 0
Tennis Racket | 13 | 0 | 1 | 0
Bottle | 71 | 0 | 9 | 0
Wine Glass | 1 | 0 | 1 | 0
Cup | 9 | 0 | 2 | 0
Fork | 0 | 0 | 0 | 0
Knife | 0 | 0 | 0 | 0
Spoon | 1 | 0 | 1 | 0
Bowl | 6 | 0 | 2 | 0
Banana | 6 | 0 | 3 | 0
Apple | 6 | 0 | 2 | 0
Sandwich | 8 | 0 | 3 | 0
Orange | 2 | 0 | 1 | 0
Broccoli | 1 | 0 | 1 | 0
Carrot | 0 | 0 | 0 | 0
Hot Dog | 1 | 0 | 1 | 0
Pizza | 4 | 0 | 2 | 0
Donut | 3 | 0 | 1 | 0
Cake | 1 | 0 | 1 | 0
Chair | 2191 | 0 | 56 | 0
Couch | 16 | 0 | 2 | 0
Potted Plant | 37917 | 0 | 406 | 7
Bed | 30 | 0 | 2 | 0
Dining Table | 133 | 0 | 9 | 0
Toilet | 30 | 0 | 3 | 0
Tv | 68 | 0 | 2 | 0
Laptop | 1 | 0 | 1 | 0
Mouse | 0 | 0 | 0 | 0
Remote | 0 | 0 | 0 | 0
Keyboard | 0 | 0 | 0 | 0
Cell Phone | 21 | 0 | 2 | 0
Microwave | 4 | 0 | 1 | 0
Oven | 6 | 0 | 1 | 0
Toaster | 0 | 0 | 0 | 0
Sink | 4 | 0 | 1 | 0
Refrigerator | 320 | 0 | 7 | 0
Book | 11 | 0 | 7 | 0
Clock | 2750 | 0 | 31 | 0
Vase | 17 | 0 | 4 | 0
Scissors | 1 | 0 | 1 | 0
Teddy Bear | 4 | 0 | 1 | 0
Hair Drier | 0 | 0 | 0 | 0
Toothbrush | 0 | 0 | 0 | 0

</details>

#### Files

File            |  Description
:-------------------------:|:-------------------------:
[total_stats.json](https://github.com/warcraft12321/RoadSafety/blob/master/yolov5/total_stats.json) |  Number of objects detected by YOLOv5 in GSV imagery by class
[lsoa_objects_number.json](https://github.com/warcraft12321/RoadSafety/blob/master/yolov5/lsoa_objects_number.json) |  Number of objects detected by YOLOv5 in GSV imagery by class and LSOA

[YOLOv5](https://github.com/ultralytics/yolov5)

### Image Segmentation

Image segmentation models reached a precision plateau (in terms of average IoU) in the previous 2 years. Due to their
long execution times, it was chosen the model executing faster and with the higher precision.

PSPNet101 was pre-trained in Cityscapes dataset. This way, it was able to label all pixels from an image across 100
categories.

<details>
  <summary>Cityscapes Categories</summary>

Void | Flat | Construction | Object | Nature | Sky | Human | Vehicle
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
Unlabeled | Road | Building | Pole | Vegetation | Sky | Person | Car
Ego Vehicle | Sidewalk | Wall | Polegroup | Terrain |  | Rider | Truck
Rectification Border | Parking | Fence | Traffic Light |  |  |  | Bus
Out of ROI | Road | Guard Rail | Traffic Sign |  |  |  | Caravan
Static |  | Bridge |  |  |  |  | Trailer
Dynamic |  | Tunnel |  |  |  |  | Train
Ground |  |  |  |  |  |  | Motorcycle
|  |  |  |  |  |  |  | Bicycle
|  |  |  |  |  |  |  | License Plate

</details>

Original            |  PSPNet101
:-------------------------:|:-------------------------:
![](./img/pspnet101/8_a.png)  |  ![](./img/pspnet101/8_a_processed.png)

[(Click to See 1 Image per LSOA)](https://drive.google.com/drive/folders/1fel8ew7h2eNJRMkXpv9lF4Zl1pydo4h-?usp=sharing)

#### Stats

#### Files

File            |  Description
:-------------------------:|:-------------------------:
[total_stats.json](https://github.com/warcraft12321/RoadSafety/blob/master/pspnet101/total_stats.json) |  Total Number of Pixels per Cityscapes Label in GSV Dataset
[rgb_label.json](https://github.com/warcraft12321/RoadSafety/blob/master/pspnet101/rgb_label) |  Conversion from RGB values to a Cityscapes label

[PSPNet101](https://github.com/hellochick/PSPNet-tensorflow)

### Supervisors
[Majid Ezzati](https://www.imperial.ac.uk/people/majid.ezzati) (Imperial College London) | [Ricky Nathvani](https://www.imperial.ac.uk/people/r.nathvani) (Imperial College London)

Featured in Towards Data Science (Medium) -> [Article](https://towardsdatascience.com/imperial-college-london-1c9bb442926)

Roadmap -> [Wiki](https://github.com/warcraft12321/RoadSafety/wiki)