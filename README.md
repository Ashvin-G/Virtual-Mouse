# Virtual Mouse
<a href="http://www.freepik.com"><img src="images/logo.jpg" width="120" height="178" align="right" alt="Designed by macrovector_official / Freepik"></a>
Virtual Mouse is a program that enables user to simulate Mouse operations such as Click, Double Click, Scroll Down, Scroll Up using Hand(Marker Less).

## Table of content
- [Prerequisite](#Prerequisite)
- [Installation](#Installation)
    - [OpenCV](#OpenCV)
    - [Numpy](#Numpy)
    - [MediaPipe](#MediaPipe)
    - [IP Webcam](#IP-Webcam)
- [Features](#Features)
  
       
   


## Prerequisite
The program was completely written using Python 3.7.0 in association with several other libraries such as OpenCV and Numpy for image processing, Google's MediaPipe library for human hand pose estimation. This program also utilizes IP Webcam Android Application for image acquisition which is freely availabale on Play Store.
> **_NOTE:_**  If the resolution and quality of builtin Webcam is good enough then there is no necessity of IP Webcam Application
>

## Installation
> **_NOTE:_**  Ensure that pip is properly installed and Python 3.7 is added to PATH
### OpenCV
The program was written without CUDA GPU support.
```
$ pip install opencv-python
```
### Numpy
```
$ pip install numpy
```
### MediaPipe
```
$ pip install mediapipe
```
### IP Webcam
<img src="images/Webcam.JPG" width="100" height="100"  alt="IP Webcam">

## Features
| Features  | Availability |
| ------------- | ------------- |
| Click  | :heavy_check_mark:  |
| Double Click  | :heavy_check_mark:  |
| Scroll Down  | :heavy_check_mark:  |
| Scroll Up  | :heavy_check_mark:  |
| Hold and Drag  | :x: |
| Scroll Left  | :x:  |
| Scroll Right | :x:  |




