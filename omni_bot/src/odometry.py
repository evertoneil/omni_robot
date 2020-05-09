#!/usr/bin/env python

import rospy
from omni_bot.msg import putaran
from omni_bot.msg import kecepatan
import math as m

#======Constant===========================
R = 0.12 # Length from Wheel to Center Point (m)
r = 0.04 # Wheel's Radius (m)
#=======Ask for input============

x = input("X (cm): ")
y = input("Y (cm) : ")
degree = input("Rotate(degree): ")
#====Convert to meter and assign as integer=================
x = float(x)/100
y = float(y)/100
degree = m.radians(int(degree))

#============INVERSE=======================================

Theta_d = 0 #in Degree sudut awal robot
Theta = m.radians(Theta_d)

#=======assign sudut roda dengan sumbu x in degree==========
a1_d = 270 #sudut roda 1 dan sumbu x
a2_d = 30 
a3_d = 150
#====convert to radians===================
a1 = m.radians(a1_d)
a2 = m.radians(a2_d)
a3 = m.radians(a3_d)
#======================================================

def talker():
    #pub = rospy.Publisher('input_posisi',input_posisi,queue_size=10)
    pub2 = rospy.Publisher('putaran',putaran,queue_size=10)
    pub3 = rospy.Publisher('kecepatan',kecepatan,queue_size=10) # send data kecepatan to driver
    rospy.init_node('odometry_inverse', anonymous=True)
    rate = rospy.Rate(10) # 10hz
#=======Inverse Calculation==================
    xr = x/r
    yr = y/r
    thetar = degree*3*R/r
    sudut1_rad = (xr*1)+(yr*0)+(thetar/3)
    sudut2_rad = (xr/-2)+(yr*m.sqrt(3)/2)+(thetar/3)
    sudut3_rad = (xr/-2)+(yr*m.sqrt(3)/-2)+(thetar/3)
#========define every motor's velocity=============
    v1 = sudut1_rad 
    v2 = sudut2_rad
    v3 = sudut3_rad
#--------penyesuaian--------------------------------------------
    vtotal = abs(v1)+abs(v2)+abs(v3)
    v1 = (v1/vtotal)*270
    v2 = (v2/vtotal)*270
    v3 = (v3/vtotal)*270
    offset = 0
#========Define Sudut yang diperlukan tiap motor================
    sudut1 = m.degrees(sudut1_rad)
    sudut2 = m.degrees(sudut2_rad)
    sudut3 = m.degrees(sudut3_rad)
#========send variable kecepatan============
    vel = kecepatan()
    vel.v1 = v1
    vel.v2 = v2
    vel.v3 = v3
#======send variable putaran needed=========
    putar = putaran()
    putar.deg1 = sudut1*6
    putar.deg2 = sudut2*6
    putar.deg3 = sudut3*6
#=========Looping and sending data===========
    while not rospy.is_shutdown():
	pub3.publish(vel)
	pub2.publish(putar)
	rate.sleep()
#============================================
#==========main program=====================
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
