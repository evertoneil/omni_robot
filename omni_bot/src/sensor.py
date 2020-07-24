#!/usr/bin/env python

#using MCP3008 as ADC Converter

import spidev 			# To communicate with SPI devices
from numpy import interp    	# To scale values
from time import sleep  	# To add delay
import RPi.GPIO as GPIO
import rospy
from omni_bot.msg import jarak	#topic dipublish dalam format ini

spi = spidev.SpiDev()
spi.open(0,0)

#================Read Analog Value===================
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
#=====================================================
def talker():
    pub = rospy.Publisher('distance', jarak, queue_size=10) 
    rospy.init_node('sensor', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    kirim = jarak()
    while not rospy.is_shutdown():
 	output = analogInput(0) 	# Reading value from CH0
	cm = 12320*pow(output,-1.073)
        if cm > 80:			#set limit to 80 cm
		cm = 80
        kirim.cm = cm
	pub.publish(kirim)		#send data to master
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
