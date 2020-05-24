#!/usr/bin/env python

import RPi.GPIO as GPIO
import pigpio

# Set the GPIO & pigpio modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pi = pigpio.pi()
#=== Set variables for the GPIO motor pins=====
Motor1_forwards = 20
Motor1_backwards = 16
Motor2_forwards = 24
Motor2_backwards = 23
Motor3_forwards = 19
Motor3_backwards = 13 
enable1 = 21
enable2 = 18 
enable3 = 26 
#=======================================================
def StopMotors():
    GPIO.output(Motor1_forwards,0)
    GPIO.output(Motor1_backwards,0)
    GPIO.output(Motor2_forwards,0)
    GPIO.output(Motor2_backwards,0)
    GPIO.output(Motor3_forwards,0)
    GPIO.output(Motor3_backwards,0)
    pi.set_PWM_dutycycle(enable1,0)
    pi.set_PWM_dutycycle(enable2,0)
    pi.set_PWM_dutycycle(enable3,0)
#=============================================
def putar():
    GPIO.output(Motor1_forwards,1)
    GPIO.output(Motor1_backwards,0)
    GPIO.output(Motor2_forwards,1)
    GPIO.output(Motor2_backwards,0)
    GPIO.output(Motor3_forwards,1)
    GPIO.output(Motor3_backwards,0)
    pi.set_PWM_dutycycle(enable1,45)
    pi.set_PWM_dutycycle(enable2,40)
    pi.set_PWM_dutycycle(enable3,50)
#=============================================
def putar2():
    GPIO.output(Motor1_forwards,0)
    GPIO.output(Motor1_backwards,1)
    GPIO.output(Motor2_forwards,0)
    GPIO.output(Motor2_backwards,1)
    GPIO.output(Motor3_forwards,0)
    GPIO.output(Motor3_backwards,1)
    pi.set_PWM_dutycycle(enable1,40)
    pi.set_PWM_dutycycle(enable2,40)
    pi.set_PWM_dutycycle(enable3,45)
      
#=============================================
    
def forwards():
    GPIO.output(Motor1_forwards,0)
    GPIO.output(Motor1_backwards,0)
    GPIO.output(Motor2_forwards,1)
    GPIO.output(Motor2_backwards,0)
    GPIO.output(Motor3_forwards,0)
    GPIO.output(Motor3_backwards,1)
    pi.set_PWM_dutycycle(enable1,0)
    pi.set_PWM_dutycycle(enable2,55)
    pi.set_PWM_dutycycle(enable3,80)
    
def backwards():
    GPIO.output(Motor1_forwards,0)
    GPIO.output(Motor1_backwards,0)
    GPIO.output(Motor2_forwards,0)
    GPIO.output(Motor2_backwards,1)
    GPIO.output(Motor3_forwards,1)
    GPIO.output(Motor3_backwards,0)
    pi.set_PWM_dutycycle(enable1,0)
    pi.set_PWM_dutycycle(enable2,58)
    pi.set_PWM_dutycycle(enable3,85)
    
def left():
    GPIO.output(Motor1_forwards,0)
    GPIO.output(Motor1_backwards,1)
    GPIO.output(Motor2_forwards,1)
    GPIO.output(Motor2_backwards,0)
    GPIO.output(Motor3_forwards,1)
    GPIO.output(Motor3_backwards,0)
    pi.set_PWM_dutycycle(enable1,128)
    pi.set_PWM_dutycycle(enable2,28)
    pi.set_PWM_dutycycle(enable3,43)
    
def right():
    GPIO.output(Motor1_forwards,1)
    GPIO.output(Motor1_backwards,0)
    GPIO.output(Motor2_forwards,0)
    GPIO.output(Motor2_backwards,1)
    GPIO.output(Motor3_forwards,0)
    GPIO.output(Motor3_backwards,1)
    pi.set_PWM_dutycycle(enable1,125)
    pi.set_PWM_dutycycle(enable2,32)
    pi.set_PWM_dutycycle(enable3,40)
    
def for_right():
    GPIO.output(Motor1_forwards,1)
    GPIO.output(Motor1_backwards,0)
    GPIO.output(Motor2_forwards,1)
    GPIO.output(Motor2_backwards,0)
    GPIO.output(Motor3_forwards,0)
    GPIO.output(Motor3_backwards,1)
    pi.set_PWM_dutycycle(enable1,40)
    pi.set_PWM_dutycycle(enable2,23)
    pi.set_PWM_dutycycle(enable3,124)

def for_left():
    GPIO.output(Motor1_forwards,0)
    GPIO.output(Motor1_backwards,1)
    GPIO.output(Motor2_forwards,1)
    GPIO.output(Motor2_backwards,0)
    GPIO.output(Motor3_forwards,0)
    GPIO.output(Motor3_backwards,1)
    pi.set_PWM_dutycycle(enable1,50)
    pi.set_PWM_dutycycle(enable2,100)
    pi.set_PWM_dutycycle(enable3,25)
    
def back_right():
    GPIO.output(Motor1_forwards,1)
    GPIO.output(Motor1_backwards,0)
    GPIO.output(Motor2_forwards,0)
    GPIO.output(Motor2_backwards,1)
    GPIO.output(Motor3_forwards,1)
    GPIO.output(Motor3_backwards,0)
    pi.set_PWM_dutycycle(enable1,55)
    pi.set_PWM_dutycycle(enable2,95)
    pi.set_PWM_dutycycle(enable3,32)

def back_left():
    GPIO.output(Motor1_forwards,0)
    GPIO.output(Motor1_backwards,1)
    GPIO.output(Motor2_forwards,0)
    GPIO.output(Motor2_backwards,1)
    GPIO.output(Motor3_forwards,1)
    GPIO.output(Motor3_backwards,0)
    pi.set_PWM_dutycycle(enable1,40)
    pi.set_PWM_dutycycle(enable2,25)
    pi.set_PWM_dutycycle(enable3,125)