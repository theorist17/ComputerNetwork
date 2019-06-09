import socket 
from socket import error as SocketError
import errno
import json
from _thread import *
import threading

mutex = threading.Lock()
queue = []
forward = True#False

def device(c):
    global forward
    global queue
    global mutex 
    dataLen = ''
    while True:
        jsondata = c.recv(1024)#.decode()
        #print(jsondata)
        if not jsondata:
            break 
        if forward and len(queue) < 10000: #10000 times of 1024bytes
            #print("appending")
            with mutex:
                queue.append(jsondata)
                #print("Append " + jsondata)
    c.close()
    print("Device off.")

def client(c):
    global forward
    global queue
    global mutex
    forward = True 
    while True:
        if queue:
            #print("forwarding")
            with mutex:
                jsondata = queue.pop(0)
                print("Pop " + jsondata.decode())
                c.sendall(jsondata)#.encode())
        #else:
            #print("empty")
    forward = False
    c.close()
    print("Client off.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 17171
s.bind(('', port))
s.listen(5)
print("Listenning...")

#device
d, addr = s.accept()
print('Got connection from'+str(addr))
start_new_thread(device, (d,))

#client
while True:
    c, addr = s.accept()
    print('Got connection from'+str(addr))
    start_new_thread(client, (c,))
c.close()
d.close()
