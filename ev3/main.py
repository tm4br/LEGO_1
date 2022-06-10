#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
#from pybricks.robotics import DriveBase
#from pybricks.media.ev3dev import SoundFile, ImageFile
from threading import Thread
import sys

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

REDIRECT = False
REDIRECTION = None
CRASH = False
STOP = False
ENGINE_SPEED = 200
NEG_ENGINE_SPEED =  0 - ENGINE_SPEED
CORRECTION_TIME = 200
ENGINE_LEFT = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
ENGINE_RIGHT = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
CS_LEFT = ColorSensor(Port.S1)
CS_RIGHT = ColorSensor(Port.S2)
TOUCH_LEFT = TouchSensor(Port.S3)
TOUCH_RIGHT = TouchSensor(Port.S4)


def path_control():
        print("Path Control launched succesfully")
        while STOP == False:
            
                
            if CS_LEFT.color() != Color.BLACK and CS_RIGHT.color() != Color.BLACK:
                REDIRECT = False
            else:
                REDIRECT = True
                #print("Redirecting = true   ")
                if CS_LEFT.color() == Color.BLACK:
                    REDIRECTION = 'left'
                    #print("redirection = left")
                else:
                    REDIRECTION = 'right'
                    #print("redirection = right")

def drive_control():
        print("Drive Control launched succesfully")
        while STOP == False:
            if CRASH == True:
                wait(100)
                
            while REDIRECT == False and CRASH == False:
                ENGINE_LEFT.run(ENGINE_SPEED)
                ENGINE_RIGHT.run(ENGINE_SPEED)
    	    
            print("REDIRECT")
            ENGINE_LEFT.hold()  
            ENGINE_RIGHT.hold()  
            
            if REDIRECTION == 'left':
                
                ENGINE_RIGHT.run(ENGINE_SPEED)
                ENGINE_LEFT.run(NEG_ENGINE_SPEED)
                wait(CORRECTION_TIME)
                ENGINE_RIGHT.hold()
                ENGINE_LEFT.hold()
            if REDIRECTION == 'right':
                ENGINE_LEFT.run(ENGINE_SPEED)
                ENGINE_RIGHT.run(NEG_ENGINE_SPEED)
                wait(CORRECTION_TIME)
                ENGINE_LEFT.hold()
                ENGINE_RIGHT.hold()

def crash_control():
        print("Crash control launched succesfully")
        while STOP == False:
            if TOUCH_RIGHT.pressed() == True or TOUCH_LEFT.pressed() == True:
                CRASH = True
                turn_back_thread = Thread(target=turn_back)
                turn_back_thread.start()

def turn_back():
        ENGINE_RIGHT.run(NEG_ENGINE_SPEED)
        ENGINE_LEFT.run(NEG_ENGINE_SPEED)
        wait(4 * CORRECTION_TIME)
        ENGINE_LEFT.run(ENGINE_SPEED)
        wait(4* CORRECTION_TIME)
        while CS_LEFT.color() != Color.BLACK:
            wait(1)
        ENGINE_RIGHT.hold()
        ENGINE_LEFT.hold()

def run():
    path_control_thread = Thread(target=path_control)
    drive_control_thread = Thread(target=drive_control)
    crash_control_thread = Thread(target=crash_control)
    path_control_thread.start()
    drive_control_thread.start()
    crash_control_thread.start()
    while STOP == False:
        wait(1000)


run()
        