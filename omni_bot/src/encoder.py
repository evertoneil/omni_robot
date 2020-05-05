#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
from omni_bot.msg import jarak

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
#=========================================
motor1_encodera = 22
motor1_encoderb = 25
motor2_encodera = 5
motor2_encoderb = 6
motor3_encodera = 17
motor3_encoderb = 27

GPIO.setup(motor1_encodera,GPIO.IN)
GPIO.setup(motor1_encoderb,GPIO.IN)
GPIO.setup(motor2_encodera,GPIO.IN)
GPIO.setup(motor2_encoderb,GPIO.IN)
GPIO.setup(motor3_encodera,GPIO.IN)
GPIO.setup(motor3_encoderb,GPIO.IN)
#=====================================================
outcome = [0,-1,1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
last_AB = 0b00
last_CD = 0b00
last_EF = 0b00
counter1 = 0
counter2 = 0
counter3 = 0
rotation3 = 0
rotation2 = 0
rotation1 = 0

#=================================================
def Encode1(): #fix
    global last_AB
    global counter1
    global rotation1
    A = GPIO.input(motor1_encodera)
    B = GPIO.input(motor1_encoderb)
    current_AB = (A << 1) | B
    position = (last_AB << 2) | current_AB
    counter1 += outcome[position]
    last_AB = current_AB
    rotation1 = counter1/60
#=================================================
def Encode2():
    global last_CD
    global counter2
    global rotation2
    C = GPIO.input(motor2_encodera)
    D = GPIO.input(motor2_encoderb)
    current_CD = (C << 1) | D
    position = (last_CD << 2) | current_CD
    counter2 += outcome[position]
    last_CD = current_CD
    rotation2 = counter2/60
#==================================================
def Encode3():
    global last_EF
    global counter3
    global rotation3
    E = GPIO.input(motor3_encodera)
    F = GPIO.input(motor3_encoderb)
    current_EF = (E << 1) | F
    position = (last_EF << 2) | current_EF
    counter3 += outcome[position]
    last_EF = current_EF
    rotation3 = counter3/60
#==============================================
def talker() :
    pub = rospy.Publisher('odometry',jarak,queue_size=10)
    rospy.init_node('encode', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    value = jarak()
    while not rospy.is_shutdown():
    	Encode3()
    	#Encode1()
   	Encode2()
	value.enc3 = rotation3
	#value.enc1 = rotation1
	value.enc2 = rotation2
	pub.publish(value)
"""
def talker():
    pub = rospy.Publisher('odometry',jarak,queue_size=10)
    rospy.init_node('encode', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	#Encode1()
	#Encode2()
	#Encode3()
	value = jarak()
    	value.enc1 = counter1
    	#value.enc2 = rotation2
    	#value.enc3 = rotation3
 	print(value.enc1)
	#rospy.loginfo(value)
        pub.publish(value)
        rate.sleep()

"""
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



