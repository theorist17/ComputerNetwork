import socket
import json
import re

#conn
serverName = '175.113.152.102'
serverPort = 17171
print("Connecting :", serverName, serverPort)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverName, serverPort))

#recv
lenString = ''
# entering in the middle of stream
while True:
    char = client.recv(1).decode()
    while char.isdigit(): # digit sequence
        lenString += char
        char = client.recv(1).decode()
    if char == '\n': # ending with line feed
        print("LENG", lenString)
        print("DATA", client.recv(int(lenString)))
        break
    else:
        lenString = ''

# parse json data
lenString = ''
data = {}
while True:
    char = client.recv(1).decode()
    while char != '\n':
        lenString += char
        char = client.recv(1).decode()
    #print("LENG", lenString)
    numToRead = int(lenString)
    lenString = '' 
    view = memoryview(bytearray(numToRead))
    nextOffset = 0
    while numToRead - nextOffset > 0:
        recvSize = client.recv_into(view[nextOffset:], numToRead - nextOffset)
        nextOffset += recvSize
    #print("DATA", view.tobytes().decode("utf-8"))
    data = json.loads(view.tobytes())
    print(data['img'])
