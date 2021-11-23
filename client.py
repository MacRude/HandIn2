import socket
from server import Server
import pickle
from emoji import emojize

HOST = ''
BufferSize = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. connect((HOST,8888))

MESSAGE = s.recv(BufferSize)
print(MESSAGE)
d = pickle.loads(MESSAGE)
print(d)
