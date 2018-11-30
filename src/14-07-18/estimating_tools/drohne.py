#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dronekit import connect, VehicleMode
import time
import rospy


connection_string = "/dev/ttyACM0" 
print "\nConnecting to vehicle on: %s" % connection_string
#vehicle = connect(connection_string, wait_ready=True)

#Callback method for new messages
def my_method(self, name, msg):
    print name, msg

#while True:
#	vehicle.add_message_listener('SYSTEM_TIME',my_method)
#	time.sleep(1)
#Create a message listener for all messages.
#@vehicle.on_message('*')
def listener(self, name, message):
    print 'message: %s' % message

while True:
	pass
vehicle.close()
