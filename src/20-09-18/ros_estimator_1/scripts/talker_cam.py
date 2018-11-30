#!/usr/bin/env python


import rospy
from std_msgs.msg import String
import drawAxis_main as dA



#init Calibration
cal = et.cam_calibration.Calibration()
#get cam param
ret, mtx, dist, rvecs, tvecs = cal.getCamParam()
#print ret, mtx, dist, rvecs, tvecs
mrk = et.aruco_marker.Marker()


def talker_cam():
    pub = rospy.Publisher('listener_cam', String, queue_size=10)
    rospy.init_node('talker_cam', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        corners , ids , rejectedImgPoints , frame, detected = mrk.detectMarkerLive()
        if detected == True:
			rvecs, tvecs, _objPoints = cv.aruco.estimatePoseSingleMarkers( corners, 0.15, mtx, dist)
			
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_cam()
    except rospy.ROSInterruptException:
        pass
