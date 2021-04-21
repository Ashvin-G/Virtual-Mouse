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
- [How To Use](#How-To-Use)
  
       
   


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
<p>IP Webcam(Developed By: Pavel Khlebovich) available freely at Play Store.</p>

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:
```bash
# Clone this repository
$ git clone https://github.com/Ashvin-G/Virtual-Mouse.git
```
### Using IP Webcam for image acquisition
Step 1: Run the IP Webcam Application and scroll down to very bottom and "Start server".<br>
Step 2: Ensure that the Mobile and Laptop/PC are on the same network. I would recommend USB tethering.<br>
Step 3: Note down the IPv4 address generated by the IP Webcam.<br>
Step 4: Edit main.py and replace<br>
```
url = "Enter your URL here/shot.jpg"
```
with your IPv4 address./
For example
```
url = http://100.73.6.196:8080/shot.jpg
```







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




