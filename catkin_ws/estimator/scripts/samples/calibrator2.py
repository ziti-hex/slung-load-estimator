#!/usr/bin/env python
#run in data calib folder 
import glob
import numpy as np
import cv2 as cv
import pathlib2
import os
import sys
import threading
import rospy
import std_msgs.msg

cap = cv.VideoCapture(0)
dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
board = cv.aruco.GridBoard_create(	markersX = 3, markersY = 3, markerLength = 0.055, markerSeparation = 0.015, dictionary = dictionary, firstMarker = 0	)
retvalw	=	cap.set(	 cv.CAP_PROP_FRAME_WIDTH , 640	)
retvalh	=	cap.set(	cv.CAP_PROP_FRAME_HEIGHT, 480	)
print('width set: %s \nheight set: %s\n' %( retvalw, retvalh) )
###  testboard1 with
###  outSize = 600,800

### take image for calibration
#
#for i in range(1):
#	while True:
#		ok,img = cap.read()
#		showcorners, showids, showrejectedImgPoints	=	cv.aruco.detectMarkers(	img, dictionary)		
#		showcorners, showids, showrejectedImgPoints	=	cv.aruco.detectMarkers(	img, dictionary)
#		showimg = cv.aruco.drawDetectedMarkers( img, showcorners )
#		
#		cv.imshow('frame',showimg)
#		if cv.waitKey(1) & 0xFF == ord('t'):
#			filename = 'calImg' + str(i) + '.jpg'
#			cv.imwrite(filename, img)
#			break




filename = 'initimg.jpg'
image = cv.imread(filename)
imageSize = image.shape[0:2]	
corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
counter = np.size(ids) 
#debug
print corners
print imageSize
print image
print counter

#debug
while True:
	showcorners, showids, showrejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
	showimg = cv.aruco.drawDetectedMarkers( image, showcorners )
	cv.imshow('frame',showimg)
	if cv.waitKey(1) & 0xFF == ord('t'):
		break


images = glob.glob('*.jpg')
calibCorners = list
calibIds = list
for fname in images:
	img = cv.imread(fname)
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
	calibCorners.append(corners)
	calibIds.append( ids )

print calibCorners
#	def getCamParam(self):
#		
#			
#			
#			# Find the chess board corners
#			ret, corners = cv.findChessboardCorners(gray, (7,6), None)
#			# If found, add object points, image points (after refining them)
#			if ret == True:
#				self.objpoints.append(self.objp)
#				corners2 = cv.cornerSubPix( gray, corners, (11,11), (-1,-1), self.criteria )
#				self.imgpoints.append(corners)
#				# Draw and display the corners
#				#cv.drawChessboardCorners(img, (7,6), corners2, ret)
#				#cv.imshow('img', img)
#				ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(self.objpoints, self.imgpoints, gray.shape[::-1], None, None)
#				return ret, mtx, dist, rvecs, tvecs








retval, cameraMatrix, distCoeffs, rvecs, tvecs	=	cv.aruco.calibrateCameraAruco(	calibCorners, ids, counter, board, imageSize, None , None)

for i in range(3):
	filename = 'calImg' + str(i) + 'jpg'
	image = cv.imread(filename)
	imageSize = image.shape[0:2]	
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
	counter = np.size(ids)
	retval, cameraMatrix, distCoeffs, rvecs, tvecs	=	cv.aruco.calibrateCameraAruco(	corners, ids, counter, board, imageSize, None , None)




#def calibrate():
#	img = cv.imread('calibPic.jpg')
#	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	img, dictionary)
#	squareMarkerLengthRate = 0.02/0.015
#	diamondCorners, diamondIds	=	cv.aruco.detectCharucoDiamond(	img, corners, ids, squareMarkerLengthRate	)
#	retval, cameraMatrix, distCoeffs, rvecs, tvecs	=	cv.aruco.calibrateCameraCharuco(diamondCorners, diamondIds, board, img.shape[0:2], None, None)
#	return cameraMatrix, distCoeffs, rvecs, tvecs
#def estimatePose(image,cameraMatrix, distCoeffs, rvecs, tvecs):
#	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
#	#print ids
#	#print corners
#	if ids != None:
#		retval_iterpolate, charucoCorners, charucoIds	=	cv.aruco.interpolateCornersCharuco(	corners, ids, image, board)
#		retval_estimatePose, rvec, tvec	=	cv.aruco.estimatePoseCharucoBoard(	charucoCorners, charucoIds, board, cameraMatrix, distCoeffs)
#		return rvec, tvec
#	return -1
#	
#if __name__ == '__main__':
#	cameraMatrix, distCoeffs, rvecs, tvecs =calibrate()
#	while True:
#		ok, image = cap.read()
#		corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
#		if ids != None:
#			retval_iterpolate, charucoCorners, charucoIds	=	cv.aruco.interpolateCornersCharuco(	corners, ids, image, board)
#			retval_estimatePose, rvec, tvec	=	cv.aruco.estimatePoseCharucoBoard(	charucoCorners, charucoIds, board, cameraMatrix, distCoeffs)
#			#image	=	cv.aruco.drawAxis(image, cameraMatrix, distCoeffs, rvec, tvec, 1	)
#			image	=	cv.aruco.drawDetectedMarkers(image, corners)
#		cv.imshow( 'window', image )
#		if cv.waitKey(1) & 0xFF == ord('q'):
#				break
#
