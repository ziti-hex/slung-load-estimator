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
from scipy.interpolate import RegularGridInterpolator
from scipy.misc import derivative
from scipy.interpolate import interp1d
from scipy import integrate

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

streamImu = file('04/imuData.yaml' , 'r')
dataImu = yaml.load(streamImu)
streamCam = file('04/imageData.yaml' , 'r')
dataCam = yaml.load(streamCam)
#uncomment for convert data in bina
npstreamImu = file('01/npimuData.npy', 'w')
np.save(npstreamImu, dataImu)

npstreamCam = file('01/npcamData.npy', 'w')
np.save(npstreamCam, dataCam)

#streamImu = file('01/npimuData.npy' , 'r')
#dataImu = np.load(streamImu)
#streamCam = file('01/npcamData.npy' , 'r')
#dataCam = np.load(streamCam)


#print (type(dataImu[0].header.stamp))
#print (len(dataCam))

def ftvec(compr_image):
	image = bridge.compressed_imgmsg_to_cv2(compr_image)
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = cam_mat, distCoeff = dist	)
	rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.1, cam_mat, dist )
	return tvecs
	 
#for compressedImage in dataCam:
#	tvecs = ftvec(compressedImage)
#	if tvecs is not None:
#		x_load.append(tvecs[0][0][0])
#		y_load.append(tvecs[0][0][1])
#		z_load.append(tvecs[0][0][2])	

x_data = []
y_data = []
z_data = []
r = 6371000.785	
for data in dataImu:
	x_data.append( data.linear_acceleration.x )
	y_data.append( data.linear_acceleration.y )
	z_data.append( data.linear_acceleration.z )



def sum_integrate(data, point):
	#print(integrate.simps(data[:point]))
	return integrate.trapz(data[:point])
	


x_integrated = []
y_integrated = []
z_integrated = [] 

for i in range(1,len(dataImu)-1, 100):
	x_integrated.append( sum_integrate(x_data, i) )
	y_integrated.append( sum_integrate(y_data, i) )
	z_integrated.append( sum_integrate(z_data, i) )

x_2integrated = []
y_2integrated = []
z_2integrated = [] 


for i in range(1,len(dataImu)-1, 100):
	x_2integrated.append( sum_integrate(x_integrated, i) )
	y_2integrated.append( sum_integrate(y_integrated, i) )
	z_2integrated.append( sum_integrate(z_integrated, i) )


ax.plot(x_data, y_data, z_data, label='copter')
ax.legend()

plt.show()

