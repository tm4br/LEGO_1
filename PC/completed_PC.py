#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor,
                                UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from threading import Thread
import socket
import threading


class EV3_Controller
    def __init__(self):
        # EV3 Hardware connect
        self.engine_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
        self.engine_right = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
        self.fS_left =  ColorSensor(Port.S1)
        self.fS_right = ColorSensor(Port.S2)
        self.touch_left = TouchSensor(Port.S3)
        self.ultrasonic = UltrasonicSensor(Port.S4)

        #Handle Threading
        self.STOP = False

        #Create Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        self.sock.bind((addr, 8484))



    #starts all Methods threaded
    def run(self):
        server_thread = threading.Thread(target=server_control)
        cam_analyse_thread = threading.Thread(target=cam_analyse)

        server_thread.start()
        cam_analyse_thread.start()

        #endless Loop so the programm does not exit
        while self.STOP == False:
            wait(1000)

Bildauswertung
    - wo ball
    - wo ev3

Ev3
    -Ev3 ausrichten
    - zu fahren
    - auf Tor ausrichten
    - schießen

socket
    - Stop
