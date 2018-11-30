#!/usr/bin/env python

## Simple listener that listens to std_msgs/Strings published 
## to the 'listener_cam' topic

import rospy
from sensor_msgs.msg import Imu

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]".
    format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener_Imu', anonymous=True)

    rospy.Subscriber('/mavros/imu/data', Imu, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
