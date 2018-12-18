#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


	
if __name__ == '__main__':
	#GPIO Modus (BOARD / BCM)
	GPIO.setmode(GPIO.BCM)
	#GPIO Pins zuweisen
	GPIO_TRIGGER = 23
	GPIO_TRIGGER_FEEDBACK = 24
	#Richtung der GPIO-Pins festlegen (IN / OUT)
	GPIO.setup(GPIO_TRIGGER, GPIO.IN)
	GPIO.setup(GPIO_TRIGGER_FEEDBACK, GPIO.OUT)

	for i in range(0, 100):
		time.sleep(0.1)	
		# setze Trigger auf HIGH
		GPIO.output(GPIO_TRIGGER_FEEDBACK, True)
		# setze Trigger nach 0.01ms aus LOW
		time.sleep(0.1)
		GPIO.output(GPIO_TRIGGER_FEEDBACK, False)
	GPIO.cleanup()
