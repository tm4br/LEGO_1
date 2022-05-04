#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

speed = 500
correction_time = 200
neg_speed = 0 - speed
engine_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
engine_right = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
fS_left =  ColorSensor(Port.S1)
fS_right = ColorSensor(Port.S2)
STOP = False

while STOP == False:
    if fS_left.color() != Color.BLACK and fS_right.color() != Color.BLACK:
        engine_left.run(speed)
        engine_right.run(speed)
    elif fS_left.color() == Color.BLACK:
        engine_right.run(speed)
        engine_left.run(neg_speed)
        wait(correction_time)
        engine_right.hold()
        engine_left.hold()
    elif fS_right.color() == Color.BLACK:
        engine_left.run(speed)
        engine_right.run(neg_speed)
        wait(correction_time)
        engine_left.hold()
        engine_right.hold()