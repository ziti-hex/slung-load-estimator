#!/usr/bin/env python

## Simple listener that listens to std_msgs/Strings published 
## to the 'listener_cam' topic
from __future__ import print_function
import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo
import sys
import cv2 as cv
import yaml
import numpy as np
from rospy.numpy_msg import numpy_msg
from estimator.msg import cam
from cv_bridge import CvBridge, CvBridgeError 

import multiprocessing


#streamCam = open('camData.yaml','w')
streamImu = open('imuData.yaml','w')
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter ('output.avi',fourcc, 20.0 , (680,480))

def callback_Imu(data):
	#dumpDataImu = [[data.orientation.x,data.orientation.y, data.orientation.z, data.orientation.w], data.header.stamp]
	yaml.dump(data,streamImu)

def listener_cam():
	while(cap.isOpened()):
		ret,frame = cap.read()
		out.write(frame)
	cap.release()
	out.release()
	
	
def listener_imu():

	rospy.init_node('listener_imu', anonymous=True)
	rospy.Subscriber('/mavros/imu/data', Imu, callback_Imu)
	rospy.spin()
	
if __name__ == '__main__':
	
	
	p_cam = multiprocessing.Process(target = listener_cam)
	p_imu = multiprocessing.Process(target = listener_imu)
	p_cam.start()
	p_imu.start()
	p_imu.join()
	p_cam.join()
	#print (threading.activeCount())
