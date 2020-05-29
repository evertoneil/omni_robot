#!/usr/bin/env python

import rospy
from omni_bot.msg import putaran
from omni_bot.msg import kecepatan
from omni_bot.msg import rpm_need
import math as m
import time
import sys
#=================Constant===========================
R = 0.12 	# Length from Wheel to Center Point (m)
r = 0.0246 	# Wheel's Radius (m)
x = 0
y = 0		
degree = 0
vx = 0
vy = 0
vt = 0
sec = 0
operand1 = 1
operand2 = 1
operand3 = 1
answer = "no"
#======================================================
Theta_d = 0 			# Degree sudut awal robot
Theta = m.radians(Theta_d)	# Convert to radian

#=======Assign sudut roda awal dengan sumbu x(degree)=====
a1_d = 270
a2_d = 30 
a3_d = 150
#=================Convert to radians===================
a1 = m.radians(a1_d)
a2 = m.radians(a2_d)
a3 = m.radians(a3_d)
#======================================================
#===============Ask for Robot's End Point==============
#======================================================
def ask():
    global x,y,degree,vx,vy,vt,sec
    print("\n===================")
    x = input("X (cm): ")
    y = input("Y (cm) : ")
    degree = input("Rotate(degree): ")
#-----------------------------------------------------
    if x==0 and y==0 and degree==0:
	print("All value are Zero !")
	x = input("X (cm): ")
    	y = input("Y (cm) : ")
    	degree = input("Rotate(degree): ")
    sec = input("Time (s) : ")
    if sec == 0:
	sec = input("Time (s) non-zero : ")
#=======Convert Input to meter and assign them as integer=====
    x = float(x)/100
    y = float(y)/100
    degree = m.radians(int(degree))
    vx = x/sec		#Robot's Velocity in X
    vy = y/sec		#Robot's Velocity in Y
    vt = degree/sec	#Robot's Angular Velocity
#======================================================
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#======================================================
def talker():
    global operand1,operand2,operand3,answer
    pub = rospy.Publisher('putaran',putaran,queue_size=10)	#Send Putaran dibutuhkan tiap motor
    pub2 = rospy.Publisher('pwm',kecepatan,queue_size=10) 	#Send PWM yang diperlukan tiap motor
    pub3 = rospy.Publisher('rpm_need',rpm_need,queue_size=10)	#Send Kecepatan diperlukan tiap motor
    rospy.init_node('odometry_inverse', anonymous=True)
    rate = rospy.Rate(10) # 10hz
#============================================================
#=======Inverse Calculation for Motor Speed==================
    v1 = ((-m.sin(Theta+a1)*m.cos(Theta)*vx) + (m.cos(Theta+a1)*m.cos(Theta)*vy)+ R*vt)/ r
    v2 = ((-m.sin(Theta+a2)*m.cos(Theta)*vx) + (m.cos(Theta+a2)*m.cos(Theta)*vy)+ R*vt)/ r
    v3 = ((-m.sin(Theta+a3)*m.cos(Theta)*vx) + (m.cos(Theta+a3)*m.cos(Theta)*vy)+ R*vt)/ r
#========Operator (-) or (+)======================
    if v1 < 0:
	operand1 = -1
    if v2 < 0:
	operand2 = -1
    if v3 < 0:
	operand3 = -1
#========Limit & Rule============================
    if abs(v1)<0.4:
	v1 = 0
    if abs(v2)<0.4:
	v2 = 0
    if abs(v3)<0.4:
	v3 = 0
#--------------------------------------------------
    v1 = abs(v1)
    v2 = abs(v2)
    v3 = abs(v3)
    v1 = 2*m.pi*r*60 * v1	#Convert rad/s to RPM
    v2 = 2*m.pi*r*60 * v2
    v3 = 2*m.pi*r*60 * v3
#=============Limit Motor===========================
    print("================= \n")
    print("RPM Motor Calculations: \n")
    print("Motor 1: " + str(v1))
    print("Motor 2: " + str(v2))
    print("Motor 3: " + str(v3))
    if v1>125 or v2>125 or v3>120:
	print("================= \n")
	print("Motor's Maximum Speed: \n")
    	print("Motor 1: 125 RPM")
   	print("Motor 2: 125 RPM")
    	print("Motor 3: 120 RPM\n")
	print("Out of Motor's Range")
	sys.exit()
    rot = rpm_need()
    rot.mot1 = v1
    rot.mot2 = v2
    rot.mot3 = v3
#==========Convert RPM to PWM=============================
#--------------------------------------------------------
#===========Equation1======================================
    if v1>0:
	v1 = (0.06641*pow(v1/10,4))-(1.5861*pow(v1/10,3))+(0.134*pow(v1,2))-(4.09365*v1) + 52.6128
    if v2>0:
    	v2 = (0.00869*pow(v2/10,5))-(0.27183*pow(v2/10,4))+(3.244*pow(v2/10,3))-(0.1748*pow(v2,2))+(4.261*v2)-12.657
    if v3>0:
    	v3 = (0.01132*pow(v3/10,5))-(0.329*pow(v3/10,4))+(3.637*pow(v3/10,3))-(0.1793*pow(v3,2))+(3.933*v3) - 5.06
#============ Equation2 =====================================
    if v1>0:
    	v1 = -(0.0003567*pow(v1/10,6))+(0.02003*pow(v1/10,5))-(0.4266*pow(v1/10,4))+(4.33262*pow(v1/10,3))-(0.2179*pow(v1,2))+(6.0868*v1) - 42.92
        if v1<45:
		v1= v1 + 4
    if v2>0:
        v2 = -(0.000309*pow(v2/10,6))+(0.01884*pow(v2/10,5))-(0.4375*pow(v2/10,4))+(4.882*pow(v2/10,3))-(0.2711*pow(v2,2))+(7.9921*v2) - 65.1171
        if v2<45:
		v2= v2 + 4
    if v3>0:
        v3 = -(0.000321*pow(v3/10,6))+(0.019703*pow(v3/10,5))-(0.46026*pow(v3/10,4))+(5.1635*pow(v3/10,3))-(0.2882*pow(v3,2))+(8.46803*v3) - 69.855
	if v3< 45 :
		v3 = v3 + 4
#==============Limit max Duty Cycle 180===============
    if v1>180:
	v1 = 180
    if v2>180:
	v2 = 180
    if v3>180:
	v3 = 180
#===============Minus/Plus=============================
    v1 = operand1 * v1
    v2 = operand2 * v2
    v3 = operand3 * v3
#=============Print PWM===============================
    print("================= \n")
    print("PWM Motor Calculations: \n")
    print("Motor 1: " + str(v1))
    print("Motor 2: " + str(v2))
    print("Motor 3: " + str(v3))
    answer = raw_input("Continue : ? (y/n) ")
    if answer== "n":
	sys.exit()
#==========send variable kecepatan=================
    vel = kecepatan()
    vel.v1 = v1
    vel.v2 = v2
    vel.v3 = v3
#==========Odometry Calculation==================
    xr = x/r
    yr = y/r
    thetar = degree*3*R/r
    sudut1_rad = (xr*1)+(yr*0)+(thetar/3)
    sudut2_rad = (xr/-2)+(yr*m.sqrt(3)/2)+(thetar/3)
    sudut3_rad = (xr/-2)+(yr*m.sqrt(3)/-2)+(thetar/3)

#========Convert Rad to Pulses================
# Rads to Rotation = Rad*0.1592
# Rotation to Pulse  = Rot*3400
# Constanta = 0.89 Berhenti lebih cepat
    putar = putaran()
    putar.deg1 = sudut1_rad*0.1592*3400*0.89
    putar.deg2 = sudut2_rad*0.1592*3400*0.89
    putar.deg3 = sudut3_rad*0.1592*3400*0.89
#=========Looping and sending all datas=======
    while not rospy.is_shutdown():
	pub2.publish(vel)
	pub.publish(putar)
	pub3.publish(rot)
#============================================
#==========main program======================
if __name__ == '__main__':
     try:
         ask()
	 talker()
     except rospy.ROSInterruptException:
         pass
