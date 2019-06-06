from socket import *

s = socket(AF_INET, SOCK_STREAM)
port = 12000
s.bind(('', port))

s.listen(5)
while True:
    c, addr = s.accept()
    try:
        print('Got connection from'+str(addr))
        message = c.recv(1024).decode()
        c.send('Thank you for connecting'.encode())
        c.close()
    except IOError:
        c.send('IOError!')
        c.close()
