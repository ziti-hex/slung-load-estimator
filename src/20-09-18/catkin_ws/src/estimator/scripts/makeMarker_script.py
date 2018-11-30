import estimating_tools as et
import cv2 as cv
import os
import pathlib2

if __name__ == '__main__':
	#init Marker with DICT_6X6_50
	
	if not os.path.exists('./data/Marker_6X6_50_300'):
					os.makedirs('./data/Marker_6X6_50_300')
					print('creating dir...')
					
	for ids in range(49):
		mrk	=	cv.aruco.drawMarker ( cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50) , ids , 300 )
		#for debug
		#cv.imshow('window', mrk)
		#cv.waitKey(500)
		
		#save marker in dir /data/Merker_6X6_50_100
		filename = "./data/Marker_6X6_50_300/marker"+ str(ids) + ".jpg" 
		cv.imwrite(filename,mrk)
		
	
