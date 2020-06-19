#!/usr/bin/env python

import time
import rospy
import RPi.GPIO as GPIO # To use GPIO pins

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

input_ls = 3
Motor1_forwards = 20
Motor1_backwards = 16
Motor2_forwards = 24 
Motor2_backwards = 23 
Motor3_forwards = 19 
Motor3_backwards = 13
#=========================================
GPIO.setup(Motor1_forwards, GPIO.OUT)
GPIO.setup(Motor1_backwards, GPIO.OUT)
GPIO.setup(Motor2_forwards, GPIO.OUT)
GPIO.setup(Motor2_backwards, GPIO.OUT)
GPIO.setup(Motor3_forwards, GPIO.OUT)
GPIO.setup(Motor3_backwards, GPIO.OUT)
GPIO.setup(input_ls, GPIO.IN)
#===========================================
count = 0.0
rospy.init_node('limit_switch')
while True:
    	A = GPIO.input(input_ls)
    	time.sleep(0.3)
    	for i in range(20):
        	count = count + A
    	count = count/30
	if count>0.68:
        	print("ok")
		GPIO.output(Motor1_forwards,GPIO.LOW)
		GPIO.output(Motor1_backwards,GPIO.LOW)
		GPIO.output(Motor2_forwards,GPIO.LOW)
		GPIO.output(Motor2_backwards,GPIO.LOW)
		GPIO.output(Motor3_forwards,GPIO.LOW)
		GPIO.output(Motor3_backwards,GPIO.LOW)
		break

