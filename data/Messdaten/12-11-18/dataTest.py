import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import yaml
import rospy
from cv_bridge import CvBridge
import cv2 as cv

bridge = CvBridge()
streamImu = file('01/imuData.yaml' , 'r')
dataImu = yaml.load(streamImu)

streamCam = file('01/imageData.yaml' , 'r')
dataCam = yaml.load(streamCam)

print(dataImu[0])
#for data in dataImu:
#	print(data.linear_acceleration)

#print(dataCam[0].header.stamp.secs,dataCam[0].header.stamp.nsecs)
#cv_image = bridge.compressed_imgmsg_to_cv2(dataCam[0])
#cv.imshow('frame', cv_image)
#cv.waitKey(200)


#print()

#for data in dataCam:
	#print(data.header.stamp.secs,data.header.stamp.nsecs)
	#cv_image = bridge.compressed_imgmsg_to_cv2(data)
	#cv.imshow('frame', cv_image)
	#cv.waitKey(200)
	
