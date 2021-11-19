import socket
import sys
import select

HOST = ''	# Symbolic name, meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port
#If want to connect to server type: telnet localhost 8888 
# in new client
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print('Socket bind complete')

#Start listening on socket
s.listen(10)
print('Socket now listening')

close_socket_condition = 0
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
	conn, addr = s.accept()
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	MESSAGE = b'Sup'

	conn.sendto(MESSAGE, (HOST, PORT))
	break


#s.close()