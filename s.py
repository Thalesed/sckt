import socket
import time

ip = input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, 1234))

s.listen(5)

clientsocket, address = s.accept()

    
while True:
    m = input('>> ')
    clientsocket.send(bytes(m, "utf-8"))
    #m = s.listen(1024)
    #print(m.decode('UTF-8'))
