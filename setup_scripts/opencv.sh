#!/bin/bash

## Bash script for setting up a Opencv development environment on Ubuntu LTS (16.04). 
##
## Installs:
## 

##  We need CMake to configure the installation, GCC for compilation, Python-devel and Numpy for building Python bindings etc.
sudo apt-get install cmake -y
sudo apt-get install python-devel numpy -y
sudo apt-get install gcc gcc-c++ -y

## Next we need GTK support for GUI features, Camera support (libv4l), Media Support (ffmpeg, gstreamer) etc.
sudo apt-get install gtk2-devel -y
sudo apt-get install libv4l-devel -y
sudo apt-get install ffmpeg-devel -y
sudo apt-get install gstreamer-plugins-base-devel -y

## Optional Dependencies
sudo apt-get install libpng-devel -y
sudo apt-get install libjpeg-turbo-devel -y
sudo apt-get install jasper-devel -y
sudo apt-get install openexr-devel -y
sudo apt-get install libtiff-devel -y
sudo apt-get install libwebp-devel -y

## Download Opencv
