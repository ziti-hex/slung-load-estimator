#!/usr/bin/env python

## Simple listener that listens to std_msgs/Strings published 
## to the 'listener_cam' topic

import rospy
import std_msgs.msg import std_msgs.msg.Float64 as float_

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener_cam', anonymous=True)

    rospy.Subscriber('talker_cam', std_msgs.msg.Float64, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener_out=listener()
    print listener_out
