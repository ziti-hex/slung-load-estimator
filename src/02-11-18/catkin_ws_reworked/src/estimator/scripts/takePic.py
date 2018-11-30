#!/usr/bin/env python
 
import numpy as np
import cv2 as cv
import glob
import os

# take image for calibration chessboard
cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)

for i in range(50):
	while True:
		ok,img = cap.read()
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		ret, showcorners = cv.findChessboardCorners(gray, (7,6), None)
		cv.drawChessboardCorners(gray, (7,6), showcorners, ret)		
		h, w = img.shape[:2]
		size = h , w
		showimg = cv.putText(img, str(size), (100,20),cv.FONT_HERSHEY_SIMPLEX,1, (50,170,50),2 )
		cv.imshow('frame',gray)
		if cv.waitKey(1) & 0xFF == ord('t'):
			if not os.path.exists('./data/calpic'):
				os.makedirs('./data/calpic')
				print('creating dir...')
			filename = './data/calpic/'+str(ret)+'calImg' + str(i) + '.jpg'
			cv.imwrite(filename, img)
			break
cap.release()

### take image for calibration aruco marker
#cap = cv.VideoCapture(0)
#dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
#for i in range(50):
#	while True:
#		ok,img = cap.read()
#		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#		showcorners, showids, rejectedImgPoints	=	cv.aruco.detectMarkers(	gray, dictionary)
#		cv.aruco.drawDetectedMarkers(gray, showcorners)		
#		h, w = img.shape[:2]
#		size = h , w
#		showimg = cv.putText(gray, str(showids), (100,20),cv.FONT_HERSHEY_SIMPLEX,0.5, (50,170,50),2 )
#		cv.imshow('frame',gray)
#		if cv.waitKey(1) & 0xFF == ord('t'):
#			filename = 'calImgAruco' + str(i) + '.jpg'
#			cv.imwrite(filename, img)
#			break
#cap.release()
#cv.destroyAllWindows()
#
