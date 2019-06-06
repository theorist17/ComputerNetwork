import socket 
import json
from _thread import *
import threading

print_lock = threading.Lock()

def device(c):
    while True:
        jsondata = c.recv(1024).decode()
        if not jsondata:
            print_lock.release()
            break
        print("Device : "+jsondata)
        jsonout = {}
        #jsonout['img'] = data.encode('base64')
        jsonout['test'] = "json is working.."
        jsondump = json.dumps(jsonout)
        c.send(jsondump.encode())
    c.close()
    print("Closed.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = gethostbyname(gethostname())
port = 17171
#print(host, port)
#s.bind((host, port))
s.bind(('', port))
s.listen(5)
print("Listenning...")
while True:
    c, addr = s.accept()
    try:
        print_lock.acquire()
        print('Got connection from'+str(addr))
        start_new_thread(device, (c,))
    except IOError:
        c.send('IOError!')
        c.close()
        print('Closed.')
