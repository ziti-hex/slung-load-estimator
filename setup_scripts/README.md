# setup_scripts
Scripts die eine Ubuntu Mschine für ROS und OpenCV konfiguriert.
## Raspbian Config 
Configuration des Raspberry-Pi für Opencv 3 mit python3 und APSync

Nötige Vorbereitung um Raspberry pi und OpenCV sowie APSync zu nutzen werden folgende 

Befehle Allgemein:
su
passwd pi
passwd root
raspi-config : tastatur layout, Land des Netzes
nano /etc/wpa_supplicant/wpa_supplicant.conf # eduroam hinzufügen
apt-get update
apt-get upgrade
rpi-update
reboot

Display:
apt-get install xinit

Befehle OpenCV und Python:
apt-get install build-essential git cmake pkg-config
apt-get install libjpeg-dev libtiff-dev libjasper-dev libpng-dev
apt-get install libavcodec-dev libavformat-dev libwscale-dev libv4l-dev v4l-utils
apt-get install libxvidcore-dev libx264-dev
apt-get install libgtk2.0-dev
apt-get install libatlas-base-dev gfortran
apt-get install python2.7-dev python2-numpy python3-dev python3-numpy
apt-get install libeigen3-dev libtbb2 libtbb-dev libdc1394-dev libdc1394-22-dev nodejs default-jre
apt-get install emscripten gstreamer-libav libavresample-dev libgphoto2-dev
sudo apt-get install libblas-dev liblapack-dev

raspi-config -- enable camera and gpu-memorysplitt set to min 128 (256)
modprobe bcm2835-v4l2 -- Enable the kernel module
permament solution add bcm2835-v4l2 to /etc/modules

nano /etc/dphys-swapfile set 100MB to 1024MB
sudo /etc/init.d/dphys-swapfile restart

swapon

Test the module with:
v4l2-ctl --list-devices
You should receive something like this:
mmal service 16.1 (platform:bcm2835-v4l2):
         /dev/video0
Test: try to grab a single frame and check for the file  ~/test.jpg
v4l2-ctl --set-fmt-video=width=800,height=600,pixelformat=3
v4l2-ctl --stream-mmap=3 --stream-count=1 --stream-to=~/test.jpg

clone open cv from git
cd ~
wget https://github.com/opencv/opencv/archive/3.4.2.zip -O opencv_source.zip
wget https://github.com/opencv/opencv_contrib/archive/3.4.2.zip -O opencv_contrib.zip
and unzip

Build and install

cmake 	-D CMAKE_BUILD_TYPE=RELEASE \
	-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules \
	-D 
        ../


ccmake ../ java und tests ausschalten ..

make
sudo make install
sudo ldconfig

pip install dronekit dronekit-sitl pyserial

sudo apt-get install python-pip python-dev python-numpy python-opencv python-serial python-pyparsing python-wxgtk2.8 libxml2-dev libxslt-dev
sudo pip install droneapi
echo "module load droneapi.module.api" >> ~/.mavinit.scr
MANUAL> api start vehicle_state.py

MAVLink on RPi

apt-get install screen python-wxgtk2.8 python-matplotlib  python-pip python-numpy python-dev libxml2-dev libxslt-dev python-lxml ## hier war noch 'python-opencv'
sudo pip install future
sudo pip install pymavlink
sudo pip install mavproxy

disable os use of serial connection  
raspi-config

Testing

sudo -s
mavproxy.py --master=/dev/ttyAMA0 --baudrate 57600 --aircraft MyCopter
sudo chown -R pi /home/pi

MAVROS installation

Configure your Ubuntu repositories

Configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse." 
Setup your computer to accept software from packages.ros.org.
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-get install dirmngr --install-recommends

Set up your keys
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

If you experience issues connecting to the keyserver, you can try substituting hkp://pgp.mit.edu:80 or hkp://keyserver.ubuntu.com:80 in the previous command.

Installation
sudo apt-get update
https://chenzhongxian.gitbooks.io/learning-robotics-using-ros/content/installing_ros_indigo_on_the_raspberry_pi.html
ROS-Base: (Bare Bones) ROS package, build, and communication libraries. No GUI tools.
sudo apt-get install ros-melodic-ros-base

Initialize rosdep

Before you can use ROS, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.

sudo rosdep init
rosdep update

Environment setup

It's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched:

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

If you just want to change the environment of your current shell, instead of the above you can type:

source /opt/ros/melodic/setup.bash

Dependencies for building packages

To install this tool and other dependencies for building ROS packages, run:
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential

## Desktop Config
Ubuntu 16


Pakete:
sudo apt-get install xinit build-essential git cmake pkg-config libjpeg-dev libtiff-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev v4l-utils libxvidcore-dev libgtk2.0-dev libx264-dev libatlas-base-dev gfortran python2.7-dev python3-dev python3-numpy libeigen3-dev libtbb2 libtbb-dev libdc1394-22-dev nodejs default-jre emscripten gstreamer1.0-libav libavresample-dev libgphoto2-dev libblas-dev liblapack-dev python-pip python-dev python-numpy python-opencv python-serial python-pyparsing python-wxgtk3.0 libxml2-dev libxslt-dev python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt-get install dirmngr --install-recommends
pip install dronekit dronekit-sitl pyserial droneapi future pymavlink mavproxy
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential python-rospy python-genpy python-roslib

Opencv : 

clone open cv from git


cd ~
wget https://github.com/opencv/opencv/archive/3.4.2.zip -O opencv_source.zip
wget https://github.com/opencv/opencv_contrib/archive/3.4.2.zip -O opencv_contrib.zip
and unzip

Build and install

cmake 	-D CMAKE_BUILD_TYPE=RELEASE \
	-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules \
	-D 
        ../


ccmake ../ java und tests ausschalten ..

make
sudo make install
sudo ldconfig


MAVROS installation

Configure your Ubuntu repositories

Configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse." 
Setup your computer to accept software from packages.ros.org.


sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

Set up your keys
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

If you experience issues connecting to the keyserver, you can try substituting hkp://pgp.mit.edu:80 or hkp://keyserver.ubuntu.com:80 in the previous command.

Installation
sudo apt-get update
https://chenzhongxian.gitbooks.io/learning-robotics-using-ros/content/installing_ros_indigo_on_the_raspberry_pi.html
ROS-Base: (Bare Bones) ROS package, build, and communication libraries. No GUI tools.
sudo apt-get install ros-melodic-ros-base

Initialize rosdep

Before you can use ROS, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.

sudo rosdep init
rosdep update

Environment setup

It's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched:

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

If you just want to change the environment of your current shell, instead of the above you can type:

source /opt/ros/melodic/setup.bash

Dependencies for building packages

To install this tool and other dependencies for building ROS packages, run:
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential

