from socket import *
serverName = '203.252.148.148' #professor's server ip addr
serverName = 'localhost'
serverName = '172.20.10.2'
serverName = '175.113.152.102'
serverPort = 12000
serverPort = 17171

print("Connecting :", serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.sendall('Hello'.encode())
print("Server : "+clientSocket.recv(1024).decode())
