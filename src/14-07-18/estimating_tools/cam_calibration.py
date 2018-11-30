import numpy as np
import cv2 as cv
import glob
import pathlib2
import os
__all__ = ['Calibration']

class Calibration():
	def __init__(self):
		self.nr = 0
		# termination criteria
		self.criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
		self.objp = np.zeros((6*7,3), np.float32)
		self.objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
		# Arrays to store object points and image points from all the images.
		self.objpoints = [] # 3d point in real world space
		self.imgpoints = [] # 2d points in image plane.
		self.images = glob.glob('data/cal_samples/*.jpg')
		
	def clean():
		cv.destroyAllWindows()
		#cap.release()
	#
	
	def getCamParam(self):
		for fname in self.images:
			img = cv.imread(fname)
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			# Find the chess board corners
			ret, corners = cv.findChessboardCorners(gray, (7,6), None)
			# If found, add object points, image points (after refining them)
			if ret == True:
				self.objpoints.append(self.objp)
				corners2 = cv.cornerSubPix( gray, corners, (11,11), (-1,-1), self.criteria )
				self.imgpoints.append(corners)
				# Draw and display the corners
				#cv.drawChessboardCorners(img, (7,6), corners2, ret)
				#cv.imshow('img', img)
				ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(self.objpoints, self.imgpoints, gray.shape[::-1], None, None)
				return ret, mtx, dist, rvecs, tvecs
				
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

		  




