#!/usr/bin/env python

from __future__ import print_function
import rospy
from sensor_msgs.msg import Imu
from sensor_msgs.msg import Image
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
import RPi.GPIO as GPIO

def setup_GPIO():
	#GPIO Modus (BOARD / BCM)
	GPIO.setmode(GPIO.BCM)
	#GPIO Pins zuweisen
	GPIO_TRIGGER = 20
	GPIO_TRIGGER_FEEDBACK = 16
	#Richtung der GPIO-Pins festlegen (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.IN)
    GPIO.setup(GPIO_TRIGGER_FEEDBACK, GPIO.OUT)

streamCam = open('camData.yaml','w')
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

	dumpDataImu = [[data.orientation.x,data.orientation.y, data.orientation.z, data.orientation.w], data.header.stamp]
	yaml.dump(dumpDataImu,streamImu)

def callback_Image(image_raw):
	
	image = bridge.imgmsg_to_cv2(image_raw,'bgr8')	
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = cam_mat, distCoeff = dist	)
	rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.105, cam_mat, dist )
	dumpDatacam =[[[tvecs],image_raw.header.stamp] ]
	yaml.dump(dumpDatacam,streamCam)
	
	#if tvecs != None:
	#	print('x = %f, y= %f z= %f ' % (tvecs[0][0][0],tvecs[0][0][1],tvecs[0][0][2] ) , end ='\r')
	#else:
	#	print ('None')
	
def listener_cam():
	
	rospy.init_node('listener_cam', anonymous=True)
	rospy.Subscriber('/camera/image_raw', Image, callback_Image)
	rospy.spin()
	
def listener_imu():

	rospy.init_node('listener_imu', anonymous=True)
	rospy.Subscriber('/mavros/imu/data', Imu, callback_Imu)
	rospy.spin()
	
if __name__ == '__main__':
	print ("starting data capture")
	setup_GPIO()
	stop_time = time.time() + 120
	
	p_cam = multiprocessing.Process(target = listener_cam)
	p_imu = multiprocessing.Process(target = listener_imu)
	p_cam.start()
	p_imu.start()
	while stop_time > time.time():
		pass
	print ("killing processes")
	p_imu.terminate()
	p_cam.terminate()
	streamCam.close()
	streamImu.close()
	print ("all worked correctly")
