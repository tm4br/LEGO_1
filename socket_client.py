import socket
import keyboard
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('127.0.0.1', 8484))
except:
    print("no connection")

connection = s.makefile('wb')

keyboard.on_press_key("w", lambda _:print("FW"))
keyboard.on_release(lambda e: print(e.name))
keyboard.on_press_key("a", lambda _:print("L"))
#keyboard.on_release("wa", lambda _:print("stop L"))
keyboard.on_press_key("s", lambda _:print("BW"))
#keyboard.on_release("s", lambda _:print("stop BW"))
keyboard.on_press_key("d", lambda _:print("R"))
#keyboard.on_release("d", lambda _:print("stop R"))
keyboard.on_press_key("ü", lambda _:print("STOP"))

while True:
    time.sleep(100)