#!/usr/bin/env python
import RPi.GPIO as GPIO
import pigpio
import time
from fungsi_joystick import putar,putar2,forwards,backwards,right,left,StopMotors,for_right,for_left,back_right,back_left
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
#===================================
Stop = 0
pi.set_PWM_frequency(enable1,25)
pi.set_PWM_frequency(enable2,25)
pi.set_PWM_frequency(enable3,25)

#====================================================
# Set the GPIO Pin mode to be Output
GPIO.setup(Motor1_forwards, GPIO.OUT)
GPIO.setup(Motor1_backwards, GPIO.OUT)
GPIO.setup(Motor2_forwards, GPIO.OUT)
GPIO.setup(Motor2_backwards, GPIO.OUT)
GPIO.setup(Motor3_forwards, GPIO.OUT)
GPIO.setup(Motor3_backwards, GPIO.OUT)
GPIO.setup(enable1, GPIO.OUT)
GPIO.setup(enable2, GPIO.OUT)
GPIO.setup(enable3, GPIO.OUT)

# Set Motor to Stop
GPIO.output(Motor1_forwards,GPIO.LOW)
GPIO.output(Motor1_backwards,GPIO.LOW)
GPIO.output(Motor2_forwards,GPIO.LOW)
GPIO.output(Motor2_backwards,GPIO.LOW)
GPIO.output(Motor3_forwards,GPIO.LOW)
GPIO.output(Motor3_backwards,GPIO.LOW)
pi.set_PWM_dutycycle(enable1,0)
pi.set_PWM_dutycycle(enable2,0)
pi.set_PWM_dutycycle(enable3,0)
#=======perbandingan
angka1 = 60  #atas_kanan= 60,30,100
angka2 = 58 #bawah_kiri= 50,25,125
angka3 = 80 #atas_kiri = 50,100,25 #bawah kanan 40,100,40

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
while True:
    x = getch()
    if x == 'w':
        StopMotors()
        time.sleep(0.5)
        forwards()
    elif x == 's':
        StopMotors()
        time.sleep(0.5)
        backwards()
    elif x == 'a':
        StopMotors()
        time.sleep(0.5)
        left()
    elif x == 'd':
        StopMotors()
        time.sleep(0.5)
        right()
    elif x == 'e':
        StopMotors()
        time.sleep(0.5)
        for_right()
    elif x == 'q':
        StopMotors()
        time.sleep(0.5)
        for_left()
    elif x == 'z':
        StopMotors()
        time.sleep(0.5)
        back_left()
    elif x == 'x':
        StopMotors()
        time.sleep(0.5)
        back_right()
    elif x == 'r':
        StopMotors()
        time.sleep(0.5)
        putar()
    elif x == 'c':
        StopMotors()
        time.sleep(0.5)
        putar2()
    elif x == 'o':
        StopMotors()
    elif x == 'p':
        StopMotors()
        break