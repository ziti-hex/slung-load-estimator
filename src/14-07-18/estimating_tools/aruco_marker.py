#!/usr/bin/env python

#making and tracking the aruco marks

from cv2 import aruco 
import cv2 as cv
import glob
import numpy as np

__all__ = ["Marker"]

class Marker():
	#@init
	#default ids = 0 , dictionary dct = DICT_6X6_1000
	
	def __init__( self, ids = 0, dct = aruco.DICT_6X6_50):
		self.ids = ids
		self.dictionary = aruco.getPredefinedDictionary(dct)
		self.markerImage = aruco.drawMarker ( self.dictionary , ids , 200 )
		self.cap = cv.VideoCapture(0)
		
	def __del__(self):
		self.cap.release()
    #@ids id of the marker in the dictionary
    #@dictionary see @13
	def makeMarker( self, ids = 0):
		retval	=	aruco.drawMarker ( self.dictionary , ids , 200 )
		return retval
	# for release capture error
	def clean(self):
		#cv.destroyAllWindows()
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

		
if __name__ == "__main__":
	print('Testing Marker class....')
	marker = Marker(0)
	lenght = 0.12
	#retval, mtx, dist, rvecs, tvecs = marker.calibrateCamera()
	while True:
		#corners , ids , rejectedImgPoints , frame , detected = marker.detectMarkerLive(marker.cap)
		#rvecs, tvecs, __objPoints = aruco.estimatePoseSingleMarkers(corners, lenght ,mtx, dist)
		#aruco.drawAxis(frame, mtx, dist, rvecs, tvecs, lenght)
		marker.drawBoxAndShow()
		if cv.waitKey(1) & 0xFF == ord('q'):
			cv.destroyAllWindows()
			break
			
	cv.destroyAllWindows()

