#!/usr/bin/env python
 
import numpy as np
import cv2 as cv
import glob
import pickle
import os
#calibration with chessboard
## termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('data/calpic/*.jpg')
#print images
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    # If found, add object points, image points (after refining them)
    #print ret
    print gray
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(50)
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
#print mtx
#img = cv.imread(images[0])
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
#print str(h) + str(w)
#print newcameramtx

#write out calibrtion data
if not os.path.exists('./data/caldata'):
	os.makedirs('./data/caldata')
	print('creating dir...')
pickle.dump(mtx, open('./data/caldata/mtx.pickle' ,'w'))
pickle.dump(dist, open('./data/caldata/dist.pickle','w'))
pickle.dump(newcameramtx, open('./data/caldata/nmtx.pickle','w'))
pickle.dump(tvecs, open('./data/caldata/tvecs.pickle','w'))
pickle.dump(rvecs, open('./data/caldata/rvecs.pickle','w'))
pickle.dump(ret, open('./data/caldata/ret.pickle','w'))
cv.destroyAllWindows()



#dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
#board = cv.aruco.GridBoard_create(	markersX = 3, markersY = 3, markerLength = 0.055, markerSeparation = 0.015, dictionary = dictionary, firstMarker = 0	)
#test board detection
#cap = cv.VideoCapture(0)
#cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
#cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
#while True:
#	ok,image = cap.read()
#	gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#	dcorners , dids, drejectedImgPoints = cv.aruco.detectMarkers( gray, dictionary )
#	if np.size(dids) == 9:
#		retval, rvec, tvec	=	cv.aruco.estimatePoseBoard(	dcorners, dids, board, newcameramtx, dist)
#		image	=	cv.aruco.drawAxis(	image, newcameramtx, dist, rvec, tvec, 0.01	)
#		print tvec
#	cv.imshow( 'window', image )
#	
#	if cv.waitKey(1) & 0xFF == ord('q'):
#			break
	
## todo
###calibration with aruco
##dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
##board = cv.aruco.GridBoard_create(	markersX = 3, markersY = 3, markerLength = 0.055, markerSeparation = 0.015, dictionary = dictionary, firstMarker = 0	)
##
##filename = 'calImgAruco23.jpg'
##image = cv.imread(filename)
##acorners , aids, arejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary)
##
##for fname in images:
##	img = cv.imread(fname)
##	newcorners, newids, newrejectedImgPoints  =	cv.aruco.detectMarkers(	img, dictionary)
##	#print np.size(newids)
##	if np.size(newids) == 9:
##		acorners = np.append(acorners, newcorners, axis = 0)
##		aids = np.append(aids, newids )
##print aids
##counter = np.size(aids)
##h, w = img.shape[:2]
##imageSize = w,h
##print counter
##print imageSize
##
##retval, cameraMatrix, distCoeffs, rvecs, tvecs	=	cv.aruco.calibrateCameraAruco(	acorners, aids, counter, board, imageSize, newcameramtx, dist, rvecs, tvecs, criteria= criteria)


