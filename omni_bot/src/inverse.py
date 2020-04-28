#!/usr/bin/env python

import rospy
from omni_bot.msg import nilai
import math as m

R = 0.12 # Length from Wheel to Center Point (m)
r = 0.04 # Wheel's Radius (m)

Theta_d = 30 #in Degree
Theta = m.radians(Theta_d)

x=1
y=2
degree=30

a1_d = 0 #degree
a2_d = 120 #degree
a3_d = 240

a1 = m.radians(a1_d)
a2 = m.radians(a2_d)
a3 = m.radians(a3_d)

v1 = ((-m.sin(Theta)*m.cos(Theta)*x) + (m.sqrt(m.cos(Theta))*y) + R*degree)/ r
v2 = ((-m.sin(Theta+a2)*m.cos(Theta)*x) + (m.cos(Theta+a2)*m.cos(Theta)*y)+ R*degree)/ r
v3 = ((-m.sin(Theta+a3)*m.cos(Theta)*x) + (m.cos(Theta+a3)*m.cos(Theta)*y)+ R*degree)/ r

def talker():
    pub = rospy.Publisher('Value',nilai,queue_size=10)
    rospy.init_node('inverse', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    value = nilai()
    value.v1 = v1
    value.v2 = v2
    value.v3 = v3
    
    while not rospy.is_shutdown():
 	rospy.loginfo(value)
        pub.publish(value)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

