#!/usr/bin/env python

import rospy
from omni_bot.msg import nilai
import math as m
import time

time_start = time.time()
second = 5

R = 0.12 # Length from Wheel to Center Point (m)
r = 0.04 # Wheel's Radius (m)

Theta_d = 0 #in Degree
Theta = m.radians(Theta_d)

x = input("X value: ")
y = input("Y value: ")
degree = input("Rotate: ")

a1_d = 0 #degree
a2_d = 120 #degree
a3_d = 240

x = int(x)
y = int(y)
degree = int(degree)

a1 = m.radians(a1_d)
a2 = m.radians(a2_d)
a3 = m.radians(a3_d)

v1 = ((-m.sin(Theta)*m.cos(Theta)*x) + (m.sqrt(m.cos(Theta))*y) + R*degree)/ r
v2 = ((-m.sin(Theta+a2)*m.cos(Theta)*x) + (m.cos(Theta+a2)*m.cos(Theta)*y)+ R*degree)/ r
v3 = ((-m.sin(Theta+a3)*m.cos(Theta)*x) + (m.cos(Theta+a3)*m.cos(Theta)*y)+ R*degree)/ r

vmotor1 = (v1/10)*33
vmotor2 = (v2/10)*30
vmotor3 = (v3/10)*60

def talker():
    pub = rospy.Publisher('Value',nilai,queue_size=10)
    rospy.init_node('inverse', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    value = nilai()
    value.v1 = vmotor1
    value.v2 = vmotor2
    value.v3 = vmotor3
    while not rospy.is_shutdown():
 	rospy.loginfo(value)
        pub.publish(value)
        rate.sleep()

def test():
    global time_start
    global second
    if (time.time()-time_start) > second:
	exit()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

