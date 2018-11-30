#!/usr/bin/env python

## Simple publisher that publish to 'listener_cam' topic


import rospy
import cv2 as cv
import pickle
import numpy as np
from rospy.numpy_msg import numpy_msg
from estimator.msg import cam

def talker_cam():
	dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
	mtx = pickle.load(open('./data/caldata/mtx.pickle','rw') )
	dist = pickle.load(open('./data/caldata/dist.pickle','rw') )
	
	cap = cv.VideoCapture(0)
	cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
	cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
	
	pub = rospy.Publisher('talker_cam', numpy_msg(cam), queue_size=10)
	rospy.init_node('talker_cam_node', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	
	while not rospy.is_shutdown():
		ok, image = cap.read()
		corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = mtx, distCoeff = dist	)
		rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.105, mtx, dist )
		#nmsg=' x='+str(tvecs[0][0][0])+', y='+str(tvecs[0][0][1])+', z='+str(tvecs[0][0][2])
		rospy.loginfo(tvecs)
		pub.publish(tvecs)	
		rate.sleep()

if __name__ == '__main__':
    try:
        talker_cam()
    except rospy.ROSInterruptException:
        pass
