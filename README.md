# Monitoring Mammalian Herbivores via Convolutional Neural Networks implemented on Thermal UAV imagery
This repository provides the code, images and annotations of the research "Monitoring Mammalian Herbivores via Convolutional Neural Networks implemented on Thermal UAV imagery".

# Algorithms
In the "algorithms" folder, scripts and tutorials for applying [TrackR-CNN](algorithms/TrackR-CNN/) and [PWC-Net](algorithms/PWC-Net/) to Multi Object Tracking and Segmentation (MOTS) are provided. **PWC-Net** is tested as an alternative tracking method to the association head used in **TrackR-CNN**.

The following flowchart illustrates the steps followed to conduct our research:

![](visualizations/Flowchart.png)

# Models
Configuration files for our models can be found in algorithms/TrackR-CNN. I use two temporal components (3D convolutions and LSTM convolutions), and two tracking mechanisms (optical flow and an association head).

## Video of TrackR-CNN results

![](visualizations/validation_dataset.gif)

## Dataset

I created my own instance segmentation dataset, which I named **COW_MOTS**, in the fashion of the [KITTI_MOTS dataset](https://www.vision.rwth-aachen.de/page/mots).

COW_MOTS consists of 7 video sequences depicting aerial thermal imagery of cattle collected with a UAV in two outdoor farms in the Netherlands. Data was acquired at three temperatures (10ºC, 19ºC and 26.,5ºC), under sunny and overcast weather conditions, at various angles of inclination (including nadir), and at heights ranging between 8-28 meters.

The COW_MOTS dataset consists of 959 frames, 20,647 masks, and 239 tracks. Ground truth was labelled manually with the Computer Vision Annotation Tool [CVAT](https://github.com/openvinotoolkit/cvat), run in a docker container.

The following images are examples of the seven datasets that comprise COW_MOTS. They illustrate data collected at different atmospheric conditions (temperature and sunlight) and angles of inclination:

<img src="visualizations/0000.png" width="270"> <img src="visualizations/0001.png" width="270">
<img src="visualizations/0002.png" width="270"> <img src="visualizations/0003.png" width="270">
<img src="visualizations/0004.png" width="270"> <img src="visualizations/0005.png" width="270">
<img src="visualizations/0006.png" width="270">

Images and annotations of **COW_MOTS** will be made publicly available soon.


