#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
#from pybricks.robotics import DriveBase
#from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
class Linedrive:
    def __init__(self):
        self.redirect = False
        self.redirection = None
        self.crash = False
        self.STOP = False
        self.engine_speed = 500
        self.neg_engine_speed = 0 - self.engine_speed
        self.correction_time =200
        self.engine_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
        self.engine_right = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        self.fS_left =  ColorSensor(Port.S1)
        self.fS_right = ColorSensor(Port.S2)
        self.touch_left = TouchSensor(Port.S3)
        self.touch_right = TouchSensor(Port.S4)
        self.turn_back_thread = threading.Thread(target=self.turn_back)

    def path_control(self):
        print("Path Control launched succesfully")
        while self.STOP == False:
            
                
            if self.fS_left.color() != Color.BLACK and self.fS_right.color() != Color.BLACK:
                self.redirect = False
            else:
                self.redirect = True
                #print("Redirecting = true   ")
                if self.fS_left.color() == Color.BLACK:
                    self.redirection = 'left'
                    #print("redirection = left")
                else:
                    self.redirection = 'right'
                    #print("redirection = right")

    def drive_control(self):
        print("Drive Control launched succesfully")
        while self.STOP == False:
            if self.crash == True:
                wait(100)
                
            while self.redirect == False and self.crash == False:
                self.engine_left.run(self.engine_speed)
                self.engine_right.run(self.engine_speed)
    	    self.engine_left.hold()  
            self.engine_right.hold()  
            
            if self.redirection == 'left':
                
                self.engine_right.run(self.engine_speed)
                self.engine_left.run(self.neg_engine_speed)
                wait(self.correction_time)
                self.engine_right.hold()
                self.engine_left.hold()
            if self.redirection == 'right':
                self.engine_left.run(self.engine_speed)
                self.engine_right.run(self.neg_engine_speed)
                wait(self.correction_time)
                self.engine_left.hold()
                self.engine_right.hold()
            

    def crash_control(self):
        print("Crash control launched succesfully")
        while self.STOP == False:
            if self.touch_right.pressed() == True or self.touch_left.pressed() == True:
                self.crash = True
                self.turn_back_thread.start()
                self.turn_back_thread.run()
                self.turn_back_thread.join()
                self.crash = False

    def turn_back(self):
        self.engine_right.run(self.neg_engine_speed)
        self.engine_left.run(self.neg_engine_speed)
        wait(4 * self.correction_time)
        self.engine_left.run(self.engine_speed)
        wait(4* self.correction_time)
        while self.fS_left.color() != Color.BLACK:
            wait(1)
        self.engine_right.hold()
        self.engine_left.hold()
    
    def run(self):
        path = threading.Thread(target=self.path_control)
        drive = threading.Thread(target=self.drive_control)
        crash = threading.Thread(target=self.crash_control)
        path.start()
        drive.start()
        crash.start()
        path.run()
        drive.run()
        crash.run()
        #path.join()
        #drive.join()
        #crash.join()


x = Linedrive()
x.run()