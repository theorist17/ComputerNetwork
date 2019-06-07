import socket
import json

#conn
serverName = '175.113.152.102'
serverPort = 17171
print("Connecting :", serverName, serverPort)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverName, serverPort))

#recv
data = {}
dataLen = ''
while True:
    char = client.recv(1).decode()
    while char != '\n':
        dataLen += char
        char = client.recv(1).decode()
    #print("LENG", dataLen)
    total = int(dataLen)
    dataLen = '' 
    view = memoryview(bytearray(total))
    nextOffset = 0
    while total - nextOffset > 0:
        recvSize = client.recv_into(view[nextOffset:], total - nextOffset)
        nextOffset += recvSize
    #print("DATA", view.tobytes().decode("utf-8"))
    data = json.loads(view.tobytes())
    print(data['img'])
