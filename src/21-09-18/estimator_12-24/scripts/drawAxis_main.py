#!/usr/bin/env python

import estimating_tools as et
import cv2 as cv
import os
import pathlib2

if __name__ == '__main__':
	#init Calibration
	cal = et.cam_calibration.Calibration()
	#get cam param
	ret, mtx, dist, rvecs, tvecs = cal.getCamParam()
	#print ret, mtx, dist, rvecs, tvecs
	mrk = et.aruco_marker.Marker()
	
	while True:
		corners , ids , rejectedImgPoints , frame, detected = mrk.detectMarkerLive()
		#print detected
		if detected == True:
			rvecs, tvecs, _objPoints = cv.aruco.estimatePoseSingleMarkers( corners, 0.15, mtx, dist)
			#print 'rvecs: ', rvecs ,'\n\n'
			#print 'tvecs: ', tvecs, '\n\n'
			print '_objPoints: ', _objPoints, '\n\n'
			cv.aruco.drawAxis(frame, mtx, dist, rvecs, tvecs, 0.1)
			#window = 'ids=%s' %(mrk.ids)
			cv.imshow( 'window' ,  frame )
			#mrk.drawBoxAndShow()
			if cv.waitKey(1) & 0xFF == ord('q'):
				break
		cv.putText(frame, "fail no marker", (100,20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);		
		cv.imshow( 'window', frame )
		if cv.waitKey(1) & 0xFF == ord('q'):
				break
	
	
