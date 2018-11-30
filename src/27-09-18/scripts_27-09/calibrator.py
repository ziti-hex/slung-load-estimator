#!/usr/bin/env python
 
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
board = cv.aruco.CharucoBoard_create(3 , 3 , 0.02 , 0.015 , dictionary)


def calibrate():
	img = cv.imread('calibPic.jpg')
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	img, dictionary)
	squareMarkerLengthRate = 0.02/0.015
	diamondCorners, diamondIds	=	cv.aruco.detectCharucoDiamond(	img, corners, ids, squareMarkerLengthRate	)
	retval, cameraMatrix, distCoeffs, rvecs, tvecs	=	cv.aruco.calibrateCameraCharuco(diamondCorners, diamondIds, board, img.shape[0:2], None, None)
	return cameraMatrix, distCoeffs, rvecs, tvecs
def estimatePose(image,cameraMatrix, distCoeffs, rvecs, tvecs):
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
	#print ids
	#print corners
	if ids != None:
		retval_iterpolate, charucoCorners, charucoIds	=	cv.aruco.interpolateCornersCharuco(	corners, ids, image, board)
		retval_estimatePose, rvec, tvec	=	cv.aruco.estimatePoseCharucoBoard(	charucoCorners, charucoIds, board, cameraMatrix, distCoeffs)
		return rvec, tvec
	return -1
	
if __name__ == '__main__':
	cameraMatrix, distCoeffs, rvecs, tvecs =calibrate()
	while True:
		ok, image = cap.read()
		corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
		if ids != None:
			retval_iterpolate, charucoCorners, charucoIds	=	cv.aruco.interpolateCornersCharuco(	corners, ids, image, board)
			retval_estimatePose, rvec, tvec	=	cv.aruco.estimatePoseCharucoBoard(	charucoCorners, charucoIds, board, cameraMatrix, distCoeffs)
			#image	=	cv.aruco.drawAxis(image, cameraMatrix, distCoeffs, rvec, tvec, 1	)
			image	=	cv.aruco.drawDetectedMarkers(image, corners)
		cv.imshow( 'window', image )
		if cv.waitKey(1) & 0xFF == ord('q'):
				break
