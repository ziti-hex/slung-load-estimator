import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import yaml
import rospy
from cv_bridge import CvBridge
import cv2 as cv

bridge = CvBridge()
streamCam = file('01/camData.yaml' , 'r')
dataCam = yaml.load(streamCam)
for data in dataCam:
	print(data.header.stamp.secs,data.header.stamp.nsecs)
	cv_image = bridge.compressed_imgmsg_to_cv2(data)
	cv.imshow('frame', cv_image)
	cv.waitKey(100)
	
