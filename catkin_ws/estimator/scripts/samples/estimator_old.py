#!/usr/bin/env python

#making and tracking the aruco marks
#cam calibration

from cv2 import aruco 
import glob
import numpy as np
import cv2 as cv
import pathlib2
import os
import threading
import rospy
import std_msgs.msg

class Estimate():
	#@init
	#default ids = 0 , dictionary dct = DICT_6X6_1000
	
	def __init__( self, ids = 0, dct = aruco.DICT_6X6_50):
		self.ids = ids
		self.dictionary = aruco.getPredefinedDictionary(dct)
		self.markerImage = aruco.drawMarker ( self.dictionary , ids , 200 )
		self.cap = cv.VideoCapture(0)
		self.nr = 0
		# termination criteria
		self.criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
		# set the dimesion of the chessboard
		self.objp = np.zeros((7*7,3), np.float32)
		self.objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)
		# Arrays to store object points and image points from all the images.
		self.objpoints = [] # 3d point in real world space
		self.imgpoints = [] # 2d points in image plane.
		self.images = glob.glob('/home/tobias/catkin_ws/data/cal_samples/*.jpg')
		
	def __del__(self):
		self.cap.release()
		
    #@ids id of the marker in the dictionary
    #@dictionary see @13
	def makeMarker( self, ids = 0):
		retval	=	aruco.drawMarker ( self.dictionary , ids , 200 )
		return retval
		
	# for release, solving capture error
	def clean(self):
		cv.destroyAllWindows()
		self.cap.release()

	def detectMarkerLive(self):
		ok, frame = self.cap.read()
		corners, ids , rejectedImgPoints = aruco.detectMarkers(frame, self.dictionary)
		if corners == []:
			detected = False
		else:
			detected = True
		return corners , ids , rejectedImgPoints , frame , detected

	def drawBoxAndShow(self):
		corners, ids , rejectedImgPoints, frame, detected = self.detectMarkerLive()
		aruco.drawDetectedMarkers(frame, corners )
		window = 'ids=%s' %(self.ids)
		cv.imshow( window, frame )
		return corners, ids, rejectedImgPoints, frame
	
	#show pic and press 't' to trigger	
	def takePhotoForCalib(self, nr = 0):
		#param nr is the numbering of the pictures
		cap = cv.VideoCapture(0)
		cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
		cap.set(cv.CAP_PROP_FRAME_HEIGHT,640)
		print('press "t" for trigger cam : ')
		while(True):
			# Capture frame-by-frame
			ret, frame = cap.read()
			# Display the resulting frame
			cv.imshow('frame',frame)
			if cv.waitKey(1) & 0xFF == ord('t'):
				if not os.path.exists('./data/cal_samples'):
					os.makedirs('./data/cal_samples')
					print('creating dir...')
				filename = "./data/cal_samples/pic"+ str(nr) + ".jpg" 
				cv.imwrite(filename,frame)
				break
		
		# When everything done, release the capture
		cap.release()
		cv.destroyAllWindows()

		
	def clean():
		cv.destroyAllWindows()
		cap.release()
	
	def getCamParam(self):
		for fname in self.images:
			img = cv.imread(fname)
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			# Find the chess board corners
			ret, corners = cv.findChessboardCorners(gray, (7,7), None)
			# If found, add object points, image points (after refining them)
			if ret == True:
				self.objpoints.append(self.objp)
				#corners2 = cv.cornerSubPix( gray, corners, (11,11), (-1,-1), self.criteria )
				self.imgpoints.append(corners)
				ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(self.objpoints, self.imgpoints, gray.shape[::-1], None, None)
				return ret, mtx, dist, rvecs, tvecs
			else:
				print 'ERROR: get cam param failed'	

	#show pic and press 't' to trigger	
	def takePhotoForCalib(self, nr = 0):
		#param nr is the numbering of the pictures
		cap = cv.VideoCapture(0)
		cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
		cap.set(cv.CAP_PROP_FRAME_HEIGHT,640)
		print('press "t" for trigger cam : ')
		while(True):
			# Capture frame-by-frame
			ret, frame = cap.read()
			# Display the resulting frame
			cv.imshow('frame',frame)
			if cv.waitKey(1) & 0xFF == ord('t'):
				if not os.path.exists('./data/cal_samples'):
					os.makedirs('./data/cal_samples')
					print('creating dir...')
				filename = "./data/cal_samples/pic"+ str(nr) + ".jpg" 
				cv.imwrite(filename,frame)
				break
		# When everything done, release the capture
		cap.release()
		cv.destroyAllWindows()

if __name__ == '__main__':
	
	#init
	est = Estimate()
	#get cam param
	ret, mtx, dist, rvecs, tvecs = est.getCamParam()
	#print ret, mtx, dist, rvecs, tvecs
	
	while True:
		corners , ids , rejectedImgPoints , frame, detected = est.detectMarkerLive()
		
		#print detected
		if detected == True:
			rvecs, tvecs, _objPoints = cv.aruco.estimatePoseSingleMarkers( corners, 0.15, mtx, dist)
			#rgb_rvec, rgb_tvec, rgb_inliers = cv.solvePnPRansac(est.objpoints, corners, mtx, dist)
			#print 'rvecs: ', rvecs ,'\n\n'
			print 'tvecs: ', tvecs, '\n\n'
			#print '_objPoints: ', _objPoints, '\n\n'
			#print rgb_tvec
			cv.aruco.drawAxis(frame, mtx, dist, rvecs, tvecs, 0.1)
			window = 'ids=%s' %(est.ids)
			cv.imshow( 'window' ,  frame )
			if cv.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			cv.putText(frame, "fail no marker", (100,20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);		
			cv.imshow( 'window', frame )
			if cv.waitKey(1) & 0xFF == ord('q'):
					break
