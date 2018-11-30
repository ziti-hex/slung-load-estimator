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


streamImu = open('imuData.yaml','w')


def callback_Imu(data):
	#rospy.loginfo(rospy.get_caller_id() + "\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]".
	#format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))

	#print(data.orientation)
	#rospy.loginfo(data.orientation)
	print(data.orientation)
	dumpDataImu = [[[data.orientation], data.header.stamp]]
	yaml.dump(dumpDataImu,streamImu)
	#print(dumpDataImu)

	
def listener_imu():

	rospy.init_node('listener_imu', anonymous=True)
	rospy.Subscriber('/mavros/imu/data', Imu, callback_Imu)
    #print "bevore spin"
    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	
if __name__ == '__main__':
	listener_imu()
	#print (threading.activeCount())
