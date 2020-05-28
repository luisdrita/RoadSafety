# Road Safety for Cyclists in London
[Jupyter Notebook](https://github.com/warcraft12321/RoadSafety/blob/master/RoadSafety.ipynb) | [Report](https://github.com/warcraft12321/RoadSafety/blob/master/text/report.pdf) | [Presentation](https://github.com/warcraft12321/RoadSafety/blob/master/text/presentation.pdf)

### Aim

The aim of this project is to use imagery to estimate safety in the roads of London, from the cyclist’s perspective. After
a brief introduction to the most important road safety indicators, it was compiled an ordered list with several risk factors. Next
step will be to determine the most appropriate pre-trained models to capture them in the images already available in Imperial servers.

### Results

#### London Image Segmentation

<img id = "img" src="./img/london.png" alt="London StreetView Imagery">
<img id = "img" src="./img/london_segmented.png" alt="London StreetView Imagery Segmented">
Used a pre-trained TensorFlow model (Xception71 model trained on Cityscapes) to segment an image of London from Imperial RDS.
[Article](https://towardsdatascience.com/street-segmentation-out-of-the-box-7df926d48e8e)

### Supervisors
[Majid Ezzati](https://www.imperial.ac.uk/people/majid.ezzati) (Imperial College London) | [Ricky Nathvani](https://www.imperial.ac.uk/people/r.nathvani) (Imperial College London)

Roadmap -> [Wiki](https://github.com/warcraft12321/RoadSafety/wiki)