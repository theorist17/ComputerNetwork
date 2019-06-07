from socket import *
serverName = '175.113.152.102'
serverPort = 17171

print("Connecting :", serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.sendall('Hello'.encode())
print("Server : "+clientSocket.recv(1024).decode())
