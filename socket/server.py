#!/usr/bin/python3

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	print('Got connection from' + str(addr))
	s.send('Thank you for connecting')
	c.close()

