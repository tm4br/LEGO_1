import socket
import time

class ControlSocket:
    def __init__(self, ev3_ip):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ev3_ip = ev3_ip
        self.STOP = False

    #connect to EV3 or wait and retries
    def connectSocket(self):
        try:
            self.sock.connect((self.ev3_ip, 8484))
            print("connected")
        except:
            print("connection failed")
            print("retry in 5s")
            time.sleep(5000)
            self.connectSocket()


    def fw(self):
        self.sock.sendall("goFW")

    def bw(self):
        self.sock.sendall("goBW")

    def rotateAngel(self, angel):
        x = "rotate "+ angel
        self.sock.sendall(x)

    def hold(self):
        self.sock.sendall("hold")

    def exit_All(self):
        self.sock.sendall("exit")
        self.sock.close()
        self.STOP = True
        exit()


    def run(self):
        self.connectSocket()
        while self.STOP == False:
            time.sleep(1000)