#!/bin/bash

## Bash script for setting up a ROS/Gazebo development environment for PX4 on Ubuntu LTS (16.04). 
## Installs:
## - ROS kinetic
## - MAVROS

## dependencies
sudo apt-get install protobuf-compiler libeigen3-dev libopencv-dev python-pathlib python-pip -y
pip install --upgrade pip
pip install pathlib2

## Setup keys
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
## For keyserver connection problems substitute hkp://pgp.mit.edu:80 or hkp://keyserver.ubuntu.com:80 above.
sudo apt-get update
## Get ROS/Gazebo
sudo apt-get install ros-kinetic-desktop-full -y
## Re/Initialize rosdep
sudo rosdep init
rosdep update
## Setup environment variables
rossource="source /opt/ros/kinetic/setup.bash"
if grep -Fxq "$rossource" ~/.bashrc; then echo ROS setup.bash already in .bashrc;
else echo "$rossource" >> ~/.bashrc; fi
eval $rossource

## Get rosinstall and other tools 
sudo apt-get install python-rosinstall build-essential ros-kinetic-ros-tutorials -y

## Install dependencies
sudo apt-get install python-wstool python-rosinstall-generator python-catkin-tools -y

## install mavros and geographiclib from onlinescript
sudo apt-get install ros-kinetic-mavros ros-kinetic-mavros-extras -y


wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
sudo chmod +x install_geographiclib_datasets.sh
sudo ./install_geographiclib_datasets.sh
rm install_geographiclib_datasets.sh
 
## Create catkin workspace
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make

## Re-source environment to reflect new packages/build environment
catkin_ws_source="source ~/catkin_ws/devel/setup.bash"
if grep -Fxq "$catkin_ws_source" ~/.bashrc; then echo ROS catkin_ws setup.bash already in .bashrc; 
else echo "$catkin_ws_source" >> ~/.bashrc; fi
eval $catkin_ws_source

if [[ ! -z $unsupported_os ]]; then
    >&2 echo -e "\033[31mYour OS ($unsupported_os) is unsupported. Assumed an Ubuntu 16.04 installation,"
    >&2 echo -e "and continued with the installation, but if things are not working as"
    >&2 echo -e "expected you have been warned."
fi

echo "printenv:"
printenv | grep ROS
echo $ROS_PACKAGE_PATH
