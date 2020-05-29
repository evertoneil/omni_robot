#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
from omni_bot.msg import counter
import time

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
#==================================================
motor1_encodera = 5
motor1_encoderb = 6 
motor2_encodera = 27 
motor2_encoderb = 17 
motor3_encodera = 25
motor3_encoderb = 22
#--------------------------------------------
GPIO.setup(motor1_encodera,GPIO.IN)
GPIO.setup(motor1_encoderb,GPIO.IN)
GPIO.setup(motor2_encodera,GPIO.IN)
GPIO.setup(motor2_encoderb,GPIO.IN)
GPIO.setup(motor3_encodera,GPIO.IN)
GPIO.setup(motor3_encoderb,GPIO.IN)
#============VARIABLE==============================
outcome = [0,1,-1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
last_AB = 0b00
last_CD = 0b00
last_EF = 0b00
counter1 = 0
counter2 = 0
counter3 = 0
count = counter()
#==================================================
#=================COUNTER==========================
def Encode1():					#Counter Motor 1
    global last_AB,counter1				
    A = GPIO.input(motor1_encodera)
    B = GPIO.input(motor1_encoderb)
    current_AB = (A << 1) | B
    position = (last_AB << 2) | current_AB
    counter1 += outcome[position]
    last_AB = current_AB
    count.enc1 = counter1
#=================================================
def Encode2():					#Counter Motor 2
    global last_CD,counter2
    C = GPIO.input(motor2_encodera)
    D = GPIO.input(motor2_encoderb)
    current_CD = (C << 1) | D
    position = (last_CD << 2) | current_CD
    counter2 += outcome[position]
    last_CD = current_CD
    count.enc2 = counter2
#=================================================
def Encode3():					#Counter Motor 3
    global last_EF,counter3
    E = GPIO.input(motor3_encodera)
    F = GPIO.input(motor3_encoderb)
    current_EF = (E << 1) | F
    position = (last_EF << 2) | current_EF
    counter3 += outcome[position]
    last_EF = current_EF
    count.enc3 = counter3
#====================================================
#=====================================================
def talker() :
    pub = rospy.Publisher('counter',counter,queue_size=5)
    rospy.init_node('encode', anonymous=True)
    while not rospy.is_shutdown():
	Encode1()
	Encode3()
	Encode2()
	pub.publish(count)			#Send Motors pulses
#============================================
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
