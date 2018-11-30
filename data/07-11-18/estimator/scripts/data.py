#!/usr/bin/env python

from __future__ import print_function
import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import CameraInfo
import sys
import cv2 as cv
import yaml
import numpy as np
from rospy.numpy_msg import numpy_msg
from estimator.msg import cam
from cv_bridge import CvBridge, CvBridgeError 
import multiprocessing
import  time




#streamTvecs = open('tvecsData.yaml','w')
streamImage = open('imageData.yaml','w')
streamImu = open('imuData.yaml','w')

with open("/home/ubuntu/.ros/camera_info/camera.yaml", 'r') as stream:
	cam_data = yaml.load(stream)
	cam_mat_lst= cam_data['camera_matrix']['data']
	cam_mat = np.zeros((3,3),dtype = float)
	cam_mat[0][0] = cam_mat_lst[0]
	cam_mat[0][1] = cam_mat_lst[1]
	cam_mat[0][2] = cam_mat_lst[2]
	cam_mat[1][0] = cam_mat_lst[3]
	cam_mat[1][1] = cam_mat_lst[4]
	cam_mat[1][2] = cam_mat_lst[5]
	cam_mat[2][0] = cam_mat_lst[6]
	cam_mat[2][1] = cam_mat_lst[7]
	cam_mat[2][2] = cam_mat_lst[8]

	dist_lst = cam_data['distortion_coefficients']['data']
	dist = np.zeros(5, dtype = float)
	for i in range(5):
		dist[i]=dist_lst[i]	

dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
bridge = CvBridge()



def callback_Imu(data):
	#dumpDataImu = [[data.orientation.x,data.orientation.y, data.orientation.z, data.orientation.w], data.header.stamp]
	yaml.dump([data],streamImu)

#def callback_Tvecs(image_raw):
#	image = bridge.imgmsg_to_cv2(image_raw,'mono16')	
#	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = cam_mat, distCoeff = dist	)
#	rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.1, cam_mat, dist )
#	dumpDataTvecs =[[[tvecs],image_raw.header.stamp] ]
#	yaml.dump(dumpDataTvecs,streamTvecs)		

def callback_Image(image):
	yaml.dump([image],streamImage)

	
def listener_cam():
	
	rospy.init_node('listener_cam', anonymous=True)
	rospy.Subscriber('/camera/image_raw/compressed', CompressedImage, callback_Image)
	rospy.spin()
	
def listener_tvecs():
	
	rospy.init_node('listener_tvecs', anonymous=True)
	rospy.Subscriber('/camera/image_raw', Image, callback_Tvecs)
	rospy.spin()

def listener_imu():

	rospy.init_node('listener_imu', anonymous=True)
	rospy.Subscriber('/mavros/imu/data', Imu, callback_Imu)
	rospy.spin()
	
if __name__ == '__main__':
	
	print ("starting data capture")
	duration = 120
	p_cam = multiprocessing.Process(target = listener_cam)
	p_imu = multiprocessing.Process(target = listener_imu)
#	p_tvecs = multiprocessing.Process(target = listener_tvecs)
	p_cam.start()
	p_imu.start()
#	p_tvecs.start()
	
	stop_time = time.time() + duration
	while stop_time > time.time():
		pass

	p_cam.terminate()
	p_imu.terminate()
#	p_tvecs.terminate()
	
	streamImu.close()
	streamImage.close()
#	streamTvecs.close()
	
	print ("all worked correctly with captureduration %i s" %(duration))
