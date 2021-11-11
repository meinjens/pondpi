#!/usr/bin/env python
# coding: latin-1

# Autor:	Ingmar Stapel
# Date:		20141229
# Version:	1.0
# Homepage:	www.raspberry-pi-car.com

import os
import sys
import termios
import tty

import L298NHBridge as HBridge

speedleft = 0
speedright = 0
speedstep = 0.05

# Instructions for when the user has an interface
print("w/s: direction")
print("a/d: steering")
print("q: stops the motors")
print("p: print motor speed (L/R)")
print("x: exit")


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def printscreen():
    # Print the motor speed just for interest
    os.system('clear')
    print("w/s: direction")
    print("a/d: steering")
    print("q: stops the motors")
    print("x: exit")
    print("========== Speed Control ==========")
    print "left motor:  ", speedleft
    print "right motor: ", speedright


while True:
    # Keyboard character retrieval method. This method will save
    # the pressed key into the variable char
    char = getch()

    if char == "w":
        # The car will drive forward when the "w" key is pressed
        # accelerate the RaPi car
        speedleft += speedstep
        speedright += speedstep

        if speedleft > 1:
            speedleft = 1
        if speedright > 1:
            speedright = 1

        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        printscreen()

    if char == "s":
        # The car will reverse when the "s" key is pressed
        # slow down the RaPi car
        speedleft -= speedstep
        speedright -= speedstep

        if speedleft < -1:
            speedleft = -1
        if speedright < -1:
            speedright = -1

        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        printscreen()

    if char == "q":
        # Stop the motors
        speedleft = 0
        speedright = 0
        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        printscreen()

    if char == "d":
        # The "d" key will toggle the steering right
        speedright -= speedstep
        speedleft += speedstep

        if speedright < -1:
            speedright = -1

        if speedleft > 1:
            speedleft = 1

        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        printscreen()

    if char == "a":
        # The "a" key will toggle the steering left
        speedleft -= speedstep
        speedright += speedstep

        if speedleft < -1:
            speedleft = -1

        if speedright > 1:
            speedright = 1

        HBridge.setMotorLeft(speedleft)
        HBridge.setMotorRight(speedright)
        printscreen()

    if char == "x":
        # The "x" key will break the loop and exit the program
        HBridge.setMotorLeft(0)
        HBridge.setMotorRight(0)
        HBridge.exit()
        print("Program Ended")
        break

    char = ""
