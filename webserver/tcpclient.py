from socket import *
serverName = '203.252.148.148' #professor's server ip addr
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverName, serverPort)
