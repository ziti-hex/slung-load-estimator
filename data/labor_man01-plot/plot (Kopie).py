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
streamImu = file('labor_man/imuData.yaml' , 'r')
dataImu = yaml.load(streamImu)
streamCam = file('labor_man/imageData.yaml' , 'r')
dataCam = yaml.load(streamCam)
x_load = [] 
y_load = []
z_load = []
x_imu = [] 
y_imu = []
z_imu = []


#print (type(dataImu[0].header.stamp))
#print (len(dataCam))

def ftvec(compr_image):
	image = bridge.compressed_imgmsg_to_cv2(compr_image)
	corners, ids, rejectedImgPoints	=	cv.aruco.detectMarkers(	image, dictionary, cameraMatrix = cam_mat, distCoeff = dist	)
	rvecs, tvecs, _objPoints	=	cv.aruco.estimatePoseSingleMarkers(	corners, 0.1, cam_mat, dist )
	return tvecs
	 
for compressedImage in dataCam:
	tvecs = ftvec(compressedImage)
	if tvecs is not None:
		x_load.append(tvecs[0][0][0])
		y_load.append(tvecs[0][0][1])
		z_load.append(tvecs[0][0][2])	



x_range = range(1,len(dataImu)-1, 1)	

def f_x(x):
	return dataImu[x].linear_acceleration.x

def f_y(x):
	return dataImu[x].linear_acceleration.y

def f_z(x):
	return dataImu[x].linear_acceleration.z

def f_interp_x():
	y=[]
	for i in x_range:
		y.append(f_x(i))
	f=interp1d(x_range,y)
	return f
def f_interp_y():
	y=[]
	for i in x_range:
		y.append(f_y(i))
	f=interp1d(x_range,y)
	return f
def f_interp_z():
	y=[]
	for i in x_range:
		y.append(f_z(i))
	f=interp1d(x_range,y)
	return f

intep_f_x = f_interp_x() 	
intep_f_y = f_interp_y() 
intep_f_z = f_interp_z()
x_integrated = []
y_integrated = []
z_integrated = [] 
integr_range = range(1,len(dataImu)-2,1)

for i in integr_range:
	x_integrated.append(integrate.quad(intep_f_x, i, i+ 1 )[1])
	y_integrated.append(integrate.quad(intep_f_y, i, i+ 1 )[1])
	z_integrated.append(integrate.quad(intep_f_z, i, i+ 1 )[1])

def f_x_integrated(x):
	return (x_integrated[x])
def f_y_integrated(x):
	return (y_integrated[x])
def f_z_integrated(x):
	return (z_integrated[x])
	
x_range_2 = range(400,len(x_integrated)-600,1)

def f_interp_x_integrated():
	y=[]
	for i in x_range_2:
		y.append(f_x_integrated(i))
	f=interp1d(x_range_2,y)
	return f
def f_interp_y_integrated():
	y=[]
	for i in x_range_2:
		y.append(f_y_integrated(i))
	f=interp1d(x_range_2,y)
	return f
def f_interp_z_integrated():
	y=[]
	for i in x_range_2:
		y.append(f_z_integrated(i))
	f=interp1d(x_range_2,y)
	return f
intep_f_x_integrated = f_interp_x_integrated() 	
intep_f_y_integrated = f_interp_y_integrated() 
intep_f_z_integrated = f_interp_z_integrated()

integr_range_2 = range(1,len(x_integrated)-3,1)
for i in integr_range_2:
	x_imu.append(integrate.quad(intep_f_x_integrated, i, i+ 1 )[1])
	y_imu.append(integrate.quad(intep_f_y_integrated, i, i+ 1 )[1])
	z_imu.append(integrate.quad(intep_f_z_integrated, i, i+ 1 )[1])


ax.plot(x_imu, y_imu, z_imu, label='Imu')
#ax.plot(x_load, y_load, z_load, label='load')

ax.legend()
plt.show()

