import socket 
import json
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
        print('Got connection from'+str(addr))
        message = c.recv(1024).decode()
        print("Client : "+message)
        jsonout = {}
        #jsonout['img'] = data.encode('base64')
        jsonout['test'] = "json is working.."
        jsonout['forwardto'] = ""
        jsondump = json.dumps(jsonout)
        c.send(jsondump.encode())
        c.close()
        print('Closed.')
    except IOError:
        c.send('IOError!')
        c.close()
        print('Closed.')
