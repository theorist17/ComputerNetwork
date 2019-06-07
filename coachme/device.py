import socket
import json

#conn
serverName = '175.113.152.102'
serverPort = 17171
print("Connecting :", serverName, serverPort)
device = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device.connect((serverName, serverPort))

#send
data = {}
i = 1
while True:
    data['img'] = i
    i += 1
    i %= 10000
    jsondata = json.dumps(data) 
    print(jsondata)
    device.send(('%d\n' % len(jsondata)).encode())
    device.sendall(jsondata.encode())
