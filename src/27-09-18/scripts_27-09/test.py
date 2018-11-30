#!/usr/bin/env python

import cv2

if __name__ == '__main__':
	
	dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
	ids = [1,2,3,4]
	squareLength = 100
	markerLength = 100
	markerImage = cv2.aruco.drawCharucoDiamond( dictionary, ids, squareLength, markerLength) 		
