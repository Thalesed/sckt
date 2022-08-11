import socket

ip = input('>> ')
p = int(input('>> '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, p))

while True:
    #m = input('>>')
    #s.send(bytes(m))
    msg = s.recv(1024)
    print(msg.decode('UTF-8'))
    #msg = input('>> ')
    #s.send(bytes(msg))
