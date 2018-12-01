#!/bin/bash

## Bash script for purge a ROS/Gazebo development environment for PX4 on Ubuntu LTS (16.04). 

# ROS melodic/Gazebo (ROS melodic includes Gazebo7 by default)
## Gazebo simulator dependencies
sudo apt-get purge protobuf-compiler libeigen3-dev libopencv-dev -y

sudo apt-get update
## Get ROS/Gazebo
sudo apt-get purge ros-melodic-desktop-full -y
## Setup environment variables
rossource="source /opt/ros/melodic/setup.bash"
## Get rosinstall
sudo apt-get purge python-rosinstall -y

## Install dependencies
sudo apt-get purge python-wstool python-rosinstall-generator python-catkin-tools -y

