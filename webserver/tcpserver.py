from socket import *
import datetime

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #tcp connection setup
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
	print("Ready to serve..\n")
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024).decode()
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = []
		outputdata.append("HTTP/1.1 200 OK\r\n")
		outputdata.append("Date: " + datetime.date.today().strftime("%B %d, %Y")+"\r\n")
		outputdata.append("\r\n")
		outputdata.append(f.read())
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.close()
	except IOError:
		outputdata = "HTTP/1.1 404 Not Found\r\n\r\nNo such file."
		connectionSocket.send(outputdata.encode())
		connectionSocket.close()
serverSocket.close()
