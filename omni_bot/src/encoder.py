#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
import RPi.GPIO as GPIO

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
motor1_encodera = 5
motor1_encoderb = 6
motor2_encodera = 17
motor2_encoderb = 27
motor3_encodera = 22
motor3_encoderb = 25

GPIO.setup(motor1_encodera,GPIO.IN)
GPIO.setup(motor1_encoderb,GPIO.IN)
GPIO.setup(motor2_encodera,GPIO.IN)
GPIO.setup(motor2_encoderb,GPIO.IN)
GPIO.setup(motor3_encodera,GPIO.IN)
GPIO.setup(motor3_encoderb,GPIO.IN)

outcome = [0,-1,1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
1last_AB = 0b00
2last_AB = 0b00
3last_AB = 0b00
counter = 0
rpm = 0
while True:
    1A = GPIO.input(motor1_encodera)
    1B = GPIO.input(motor1_encoderb)
    2A = GPIO.input(motor1_encodera)
    2B = GPIO.input(motor1_encoderb)
    3A = GPIO.input(motor1_encodera)
    3B = GPIO.input(motor1_encoderb)
    1current_AB = (1A << 1) | 1B
    1position = (2last_AB << 2) | 1current_AB
    1counter += outcome[1position]
    1last_AB = 1current_AB
#===============================================
    2current_AB = (2A << 1) | 2B
    2position = (2last_AB << 2) | 2current_AB
    2counter += outcome[2position]
    2last_AB = 2current_AB
#===============================================
    3current_AB = (3A << 1) | 3B
    3position = (3last_AB << 2) | 3current_AB
    3counter += outcome[3position]
    3last_AB = 3current_AB
    print (1counter)
    print (2counter)
    print (3counter)


