import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('192.168.117.1', 8483))

while True: 
    socket.listen()
    print("now listening")
    conn, addr = socket.accept()
    while True:
        data = conn.recv(1024)
        print("incomming Message: ", data)
        if data == b"FW":
            go_FW()