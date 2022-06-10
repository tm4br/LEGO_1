import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("127.0.0.1", 8484))

while True: 
    self.sock.listen()
    print("now listening")
    conn, addr = socket.accept()
    while True:
        data = conn.recv(1024)
        print("incomming Message: ", data)
        if data == "FW":
            go_FW