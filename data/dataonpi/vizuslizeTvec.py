
import pickle
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import yaml
import rospy
from cv_bridge import CvBridge
import cv2 as cv
import  time


dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
mtx = pickle.load(open('../caldata/mtx.pickle','rw') )
dist = pickle.load(open('../caldata/dist.pickle','rw') )

bridge = CvBridge()
streamCam = file('01/imageData.yaml' , 'r')
dataCam = yaml.load(streamCam)
i = 0

for data in dataCam:
	print(data.header.stamp.secs,data.header.stamp.nsecs)
	print (i) 
	i = i + 1
	image = bridge.compressed_imgmsg_to_cv2(data)
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = mtx, distCoeff = dist	)
	rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.1, mtx, dist )
	if np.size(ids) != 0:
		#print ids
		image	=	cv.aruco.drawDetectedMarkers(	image, corners	)
		#print tvecs
		pmessage = 'distance'+str(tvecs)	
	cv.putText(image, pmessage, (10,20), cv.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0),1)
	cv.imshow('frame', image)
	cv.waitKey(100)
