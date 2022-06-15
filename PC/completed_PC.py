import socket
import keyboard
import time
from controlSocket import ControlSocket
import cv2



class PC_Controller:
    def __init__(self):
        self.sock = ControlSocket('192.168.117.1')
        self.sock.run()




    def frame_analysis(self):
        self.sock.fw()
        self.sock.bw()
        self.sock.rotateAngel(1)
        self.sock.hold()
        self.sock.exit_All()
        self.sock.set_speed(200)
        




    def run(self):
        self.frame_analysis()
