#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor,
                                UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from threading import Thread


ev3 = EV3Brick()

Matrix1 = [[6,5,4,3,2,1,2,3],
            [5,4,3,2,1,0,1,2],
            [6,5,4,3,2,1,2,3],
            [7,6,5,4,3,2,3,4],
            [8,7,6,5,4,3,4,5],
            [9,8,7,6,5,4,5,6],
            [10,9,8,7,6,5,6,7],
            [11,10,9,8,7,6,7,8],
            [12,11,10,9,8,7,8,9],
            [13,12,11,10,9,8,9,10],
            [14,13,12,11,10,9,10,11]]


'''
6 5 4 3 2 1 2 3
5 4 3 2 1 0 1 2
6 5 4 3 2 1 2 3
7 6 5 4 3 2 3 4
8 7 6 5 4 3 4 5
9 8 7 6 5 4 5 6
10 9 8 7 6 5 6 7
11 10 9 8 7 6 7 8
12 11 10 9 8 7 8 9
13 12 11 10 9 8 9 10
14 13 12 11 10 9 10 11
'''


engine_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
engine_right = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        



class Bahnplanung:
    def __init__(self, matrix, start_x, start_y):
        self.direction = FW
        self.matrix = matrix
        self.start_x = start_x
        self.start_y = start_y
        self.engine_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
        self.engine_right = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        self.fS_left =  ColorSensor(Port.S1)
        self.fS_right = ColorSensor(Port.S2)
        self.touch_left = TouchSensor(Port.S3)
        self.ultrasonic = UltrasonicSensor(Port.S4)
        self.engine_speed = 200
        self.neg_engine_speed = 0 - self.engine_speed
        self.field_length = 200
        self.drive_time_to_next_field = field_length / 0.0738

    
    def find_path(self):
        pass

    def turn_right(self):
        self.engine_left.run(200)
        self.engine_right.run(-200)
        wait(2900)
        self.engine_left.stop()
        self.engine_right.stop() 
    
    def turn_left(self):
        self.engine_left.run(-200)
        self.engine_right.run(200)
        wait(2900)
        self.engine_left.stop()
        self.engine_right.stop() 
    
    def turn_back(self):
        self.engine_left.run(200)
        self.engine_right.run(-200)
        wait(4800)
        self.engine_left.stop()
        self.engine_right.stop() 

    def go_FW(self):
        engine_right.run(self.engine_speed)
        engine_right.run(self.engine_speed)
        wait(drive_time_to_next_field)
        engine_right.stop()
        engine_left.stop()

    def run(self):
        pass


'''
engine_left.run(200)
engine_right.run(-200)
wait(2900)
engine_left.stop()
engine_right.stop()
'''

bp = Bahnplanung(Matrix1, 10, 7)