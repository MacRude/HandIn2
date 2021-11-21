import socket
HOST = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. connect((HOST,8888))
MESSAGE = s.recv(1024)
print(MESSAGE.decode())