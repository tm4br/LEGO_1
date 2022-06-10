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
        self.direction = 'FW'
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
        self.drive_time_to_next_field = self.field_length / 0.0735

    
    def find_path(self):
        print("pathfindng start")
        x = self.start_x
        y = self.start_y
        value = self.matrix[x][y]
        value_front = 1000
        value_right = 1000
        value_left = 1000
        value_back = 1000
        value_list = [value_front, value_right, value_back, value_left]
        while value != 0:
            print("field [",x,"][",y,"]")
            try:
                value_front = matrix[x][y-1]
            except:
                value_front = 1000
            try:
                value_right = matrix[x+1][y]
            except:
                value_right = 1000
            try:
                value_left = matrix[x-1][y]
            except:
                value_left = 1000
            try:
                value_back = matrix[x][y+1]
            except:
                value_back = 1000


            lowest = 1000
            lowest_direction = None
            if value_front < lowest:
                lowest = value_front
                lowest_direction = 'FW'
            if value_right < lowest:
                lowest = value_right
                lowest_direction = 'R'
            if value_back < lowest:
                lowest = value_back
                lowest_direction = 'BW'
            if value_left < lowest:
                lowest = value_left
                lowest_direction = 'L'

            if lowest_direction ==  'FW':
                self.go_FW()
                y = y-1
            elif lowest_direction == 'R':
                self.go_right()
                x = x+1
            elif lowest_direction == 'L':
                self.go_left()
                x = x-1
            elif lowest_direction == 'BW':
                self.go_back()
                x = y+1



         

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
        print("go FW")
        engine_right.run(self.engine_speed)
        engine_left.run(self.engine_speed)
        wait(self.drive_time_to_next_field)
        engine_right.stop()
        engine_left.stop()
    
    def go_right(self):
        print("go right")
        if self.direction == 'FW':
            self.turn_right()
            self.go_FW()
        elif self.direction == 'R':
            self.go_FW()
        elif self.direction == 'L':
            self.turn_back()
            self.go_FW()
        elif self.direction == 'BW':
            self.turn_left()
            self.go_FW()

        self.direction = 'R'
        
    def go_left(self):
        print("go left")
        if self.direction == 'FW':
            self.turn_left()
            self.go_FW()
        if self.direction == 'L':
            self.go_FW()
        if self.direction == 'R':
            self.turn_back()
            self.go_FW()
        if self.direction == 'BW':
            self.turn_right()
            self.go_FW()
        self.direction = 'L'

    def go_back(self):
        print("go back")
        if self.direction == 'FW':
            self.turn_back()
            self.go_FW()
        if self.direction == 'BW':
            self.go_FW()
        if self.direction == 'R':
            self.turn_right()
            self.go_FW()
        if self.direction == 'L':
            self.turn_left()
            self.go_FW()
        self.direction = 'BW'



    def run(self):
        print("run")
        self.find_path()



'''
engine_left.run(200)
engine_right.run(-200)
wait(2900)
engine_left.stop()
engine_right.stop()
'''

bp = Bahnplanung(Matrix1, 10, 7)
bp.run()