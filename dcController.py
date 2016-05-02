#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import readchar
import sys
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def moveForward():
    myMotorR.run(Adafruit_MotorHAT.RELEASE);
    myMotorL.run(Adafruit_MotorHAT.RELEASE);
    myMotorL.run(Adafruit_MotorHAT.FORWARD)
    myMotorR.run(Adafruit_MotorHAT.FORWARD)

def moveBackward():
    myMotorR.run(Adafruit_MotorHAT.RELEASE)
    myMotorL.run(Adafruit_MotorHAT.RELEASE)
    myMotorL.run(Adafruit_MotorHAT.BACKWARD)
    myMotorR.run(Adafruit_MotorHAT.BACKWARD)

def moveLeft():
    myMotorR.run(Adafruit_MotorHAT.RELEASE)
    myMotorL.run(Adafruit_MotorHAT.RELEASE)
    myMotorR.run(Adafruit_MotorHAT.FORWARD)
    myMotorL.run(Adafruit_MotorHAT.BACKWARD)

def moveRight():
    myMotorR.run(Adafruit_MotorHAT.RELEASE)
    myMotorL.run(Adafruit_MotorHAT.RELEASE)
    myMotorL.run(Adafruit_MotorHAT.FORWARD)
    myMotorR.run(Adafruit_MotorHAT.BACKWARD)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotorL = mh.getMotor(4)
myMotorR = mh.getMotor(1)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotorL.setSpeed(150)
myMotorR.setSpeed(150)

while (True):
    line = sys.stdin.readline()

    if line == 'forward\n':
        moveForward()
    elif line == 'left\n':
        moveLeft()
    elif line == 'right\n':
        moveRight()
    elif line == 'back\n':
        moveBackward()
    elif line == 'stop\n':
        turnOffMotors()
