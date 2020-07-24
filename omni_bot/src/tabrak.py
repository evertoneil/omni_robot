#!/usr/bin/env python

import time
import rospy
import RPi.GPIO as GPIO # To use GPIO pins

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

input_ls = 3 # pin input deteksi limit switch / tabrakan
count = 0.0 

while True:
    	A = GPIO.input(input_ls)
    	time.sleep(0.3)
#agar input dapat terbaca, maka dibuat rata-rata kondisi limit switch
    	for i in range(20):
        	count = count + A
    	count = count/30
#angka 0 kondisi limit switch tidak ditekan
#angka diatas 0.68 berarti limit switch ditekan
#angka 0.68 diambil dari trial & error
	if count>0.68:
        	print("ok")
		break

