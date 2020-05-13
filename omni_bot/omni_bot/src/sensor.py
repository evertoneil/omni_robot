#!/usr/bin/env python
import spidev # To communicate with SPI devices
from numpy import interp    # To scale values
from time import sleep  # To add delay
import RPi.GPIO as GPIO # To use GPIO pins
import rospy
from omni_bot.msg import jarak

spi = spidev.SpiDev() # Created an object
spi.open(0,0)
   
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def talker():
    pub = rospy.Publisher('distance', jarak, queue_size=10)
    rospy.init_node('sensor', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    kirim = jarak()
    while not rospy.is_shutdown():
 	output = analogInput(0) # Reading from CH0
	cm = 12320*pow(output,-1.073)
        #cm = pow(3027.4/output,1.2)
	if cm > 80:
		cm = 80
        kirim.cm = cm
	rospy.loginfo(kirim)
	pub.publish(kirim)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
