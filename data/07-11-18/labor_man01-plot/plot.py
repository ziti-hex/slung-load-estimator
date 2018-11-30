import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import yaml
import rospy
import pickle
from cv_bridge import CvBridge
import cv2 as cv
import  time

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()


dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_6X6_50)
with open("/home/tobias/.ros/camera_info/camera.yaml", 'r') as stream:
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
		
bridge = CvBridge()
ax = fig.gca(projection='3d')
streamImu = file('labor_man/imuData.yaml' , 'r')
dataImu = yaml.load(streamImu)
xa = []
ya = []
za = []
#time = []
#print (type(dataImu[0].orientation))
for data in dataImu:
	xa.append(data.orientation.x)
	ya.append(data.orientation.y)
	za.append(data.orientation.z)
	#time.append()
ax.plot(xa, ya, za, label='Imu')

streamCam = file('labor_man/imageData.yaml' , 'r')
dataCam = yaml.load(streamCam)
xb = []
yb = []
zb = []	

for data in dataCam:
	image = bridge.compressed_imgmsg_to_cv2(data)
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = cam_mat, distCoeff = dist	)
	rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.1, cam_mat, dist )

	if tvecs != None:
		xb.append(tvecs[0][0][0])
		yb.append(tvecs[0][0][1])
		zb.append(tvecs[0][0][2])	

ax.plot(xb, yb, zb, label='Cam')

ax.legend()
plt.show()
