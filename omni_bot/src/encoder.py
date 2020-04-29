#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
import RPi.GPIO as GPIO

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
motor1_encodera = 5
motor1_encoderb = 6
motor2_encodera = 22
motor2_encoderb = 25
motor3_encodera = 17
motor3_encoderb = 27

GPIO.setup(motor1_encodera,GPIO.IN)
GPIO.setup(motor1_encoderb,GPIO.IN)
GPIO.setup(motor2_encodera,GPIO.IN)
GPIO.setup(motor2_encoderb,GPIO.IN)
GPIO.setup(motor3_encodera,GPIO.IN)
GPIO.setup(motor3_encoderb,GPIO.IN)

outcome = [0,-1,1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
last_AB = 0b00
last_CD = 0b00
last_EF = 0b00
counter1 = 0
counter2 = 0
counter3 = 0

def Encode1():
    global last_AB
    global counter1
    A = GPIO.input(motor1_encodera)
    B = GPIO.input(motor1_encoderb)
    current_AB = (A << 1) | B
    position = (last_AB << 2) | current_AB
    counter1 += outcome[position]
    last_AB = current_AB
    print("A="+ str(counter1))

def Encode2():
    global last_CD
    global counter2
    C = GPIO.input(motor2_encodera)
    D = GPIO.input(motor2_encoderb)
    current_CD = (C << 1) | D
    position = (last_CD << 2) | current_CD
    counter2 += outcome[position]
    last_CD = current_CD
    print("B="+ str(counter2))

def Encode3():
    global last_EF
    global counter3
    E = GPIO.input(motor3_encodera)
    F = GPIO.input(motor3_encoderb)
    current_EF = (E << 1) | F
    position = (last_EF << 2) | current_EF
    counter3 += outcome[position]
    last_EF = current_EF
    print("C="+ str(counter3))

while True:
    Encode2()
    Encode3()
    Encode1()


