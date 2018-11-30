#!/usr/bin/env python

## Simple listener that listens to std_msgs/Strings published 
## to the 'listener_cam' topic
from __future__ import print_function
import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo
import sys
import cv2 as cv
import yaml
import numpy as np
from rospy.numpy_msg import numpy_msg
from estimator.msg import cam
from cv_bridge import CvBridge, CvBridgeError 
import  time


import multiprocessing

streamCam = open('camData.yaml','w')
streamImu = open('imuData.yaml','w')

bridge = CvBridge()



def callback_Imu(data):

	#print(data.orientation)
	#dumpDataImu = [[data.orientation.x,data.orientation.y, data.orientation.z, data.orientation.w], data.header.stamp]
	#print('got Imu')
	dumpdata = [data]
	yaml.dump(dumpdata,streamImu)
	#print(dumpDataImu)
	#if time.time()> stop_time:
	#	p_imu.terminate()

def callback_Image(image_raw):
	#print (image_raw.header)
	#image = bridge.imgmsg_to_cv2(image_raw,'bgr8')	
	#print('got Image')
	dumpdata = [image_raw]
	yaml.dump(dumpdata ,streamCam)
	#if time.time() > stop_time:
	#	p_cam.terminate()
def listener_cam():
	#print('cam node')
	rospy.init_node('listener_cam', anonymous=True)
	rospy.Subscriber('/camera/image_raw/compressed', CompressedImage, callback_Image)
	rospy.spin()
	
def listener_imu():
	#print('imu node')
	rospy.init_node('listener_imu', anonymous=True)
	rospy.Subscriber('/mavros/imu/data', Imu, callback_Imu)
    #print "bevore spin"
    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	
if __name__ == '__main__':
	print ("starting data capture")
	stop_time = time.time() + 120
	#while stop_time < time.time() + 120:
	p_cam = multiprocessing.Process(target = listener_cam)
	p_imu = multiprocessing.Process(target = listener_imu)
	p_cam.start()
	p_imu.start()
	while stop_time > time.time():
		pass
	print ("killing processes")
	p_imu.terminate()
	p_cam.terminate()
	print ("all worked correctly")
	
	
