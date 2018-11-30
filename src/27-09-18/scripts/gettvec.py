#!/usr/bin/env python

import cv2 as cv
import pickle
import numpy as np

if __name__ == '__main__':
	
	dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
	mtx = pickle.load(open('./data/caldata/mtx.pickle','rw') )
	dist = pickle.load(open('./data/caldata/dist.pickle','rw') )
	cap = cv.VideoCapture(0)
	cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
	cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
	while True:
		ok, image = cap.read()
		corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = mtx, distCoeff = dist	)
		rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.12, mtx, dist )
		if np.size(ids) != 0:
			print ids
			image	=	cv.aruco.drawDetectedMarkers(	image, corners	)
			print tvecs
			pmessage = 'distance'+str(tvecs)	
		cv.putText(image, pmessage, (10,20), cv.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0),1)
		cv.imshow('frame', image)
		if cv.waitKey(1) & 0xFF == ord('q'):
			break
