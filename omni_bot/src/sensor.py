#!/usr/bin/env python
import spidev # To communicate with SPI devices
from numpy import interp    # To scale values
from time import sleep  # To add delay
import RPi.GPIO as GPIO # To use GPIO pins
import rospy
from std_msgs.msg import Int16

spi = spidev.SpiDev() # Created an object
spi.open(0,0)
   
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def talker():
    pub = rospy.Publisher('distance', Int16, queue_size=10)
    rospy.init_node('sensor', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
 	output = analogInput(0) # Reading from CH0
    	output = interp(output, [0, 1023], [0, 100])
        rospy.loginfo(output)
        pub.publish(output)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
