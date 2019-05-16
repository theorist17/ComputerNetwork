from socket import *
import ssl
# Message to send
msg = '\r\n I love Konkuk University'
endmsg = '\r\n.\r\n'

# Choose your mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'


##### begin to add #####
# Create a TCP socket called clientSocket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to the mailserver with port number 587 (Port number may change according to the mail server)
clientSocket.connect((mailserver, 587))
# Save the received message (from server) to 'recv'
recv = clientSocket.recv(1024)
# Print recv
print(recv.decode())
##### end to add #####
if recv[:3] != '220':
	print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO www.gmail.com\r\n'
##### begin to add #####
# Send heloCommand down through clientSocket
clientSocket.send(heloCommand.encode())
# Save the received message (from server) to 'recv1'
recv1 = clientSocket.recv(1024)
# Print 'recv1'
print(recv1.decode())
##### end to add #####
if recv1[:3] != '250':
	print('1 250 reply not received from server.')

# Request an encrypted connection
startTlsCommand = 'STARTTLS\r\n'
clientSocket.send(startTlsCommand.encode())
tls_recv = clientSocket.recv(1024)
print(tls_recv)
if tls_recv[:3] != '220':
	print('220 reply not received from server')

# Encrypt the socket
ssl_clientSocket = socket.ssl(clientSocket)

# Send the AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
ssl_clientSocket.write(authCommand)
auth_recv = ssl_clientSocket.read(1024)
print(auth_recv.decode())
if auth_recv[:3] != '334':
	print('334 reply not received from server')

# Send username and print server response.
uname = base64.b64encode(username) + '\r\n'
ssl_clientSocket.write(uname)
uname_recv = ssl_clientSocket.read(1024)
print(uname_recv.decode)
if uname_recv[:3] != '334':
	print('334 reply not received from server')

# Send password and print server response.
pword = base64.b64encode(password) + '\r\n'
ssl_clientSocket.write(pword)
pword_recv = ssl_clientSocket.read(1024)
print(pword_recv.decode())
if pword_recv[:3] != '235':
	print('235 reply not received from server')

# Send MAIL FROM command and print server response.
mailfrom = 'MAIL FROM: <theorist17@gmail.com>\r\n'
##### begin to add #####
# Send mailfrom down through clientSocket
clientSocket.send(mailfrom.encode())
# Save the received message (from server) to 'recv2'
recv2 = clientSocket.recv(1024)
# Print 'recv2'
print(recv2.decode())
##### end to add #####
if recv2[:3] != '250':
	print('2 250 reply not received from server.')


# Send RCPT TO command and print server response. 
rcptto = 'RCPT TO: <theorist17@naver.com>\r\n'
##### begin to add #####
# Send rcptto down through clientSocket
clientSocket.send(rcptto.encode())
# Save the received message (from server) to 'recv3'
recv3 = clientSocket.recv(1024)
# Print 'recv3'
print(recv3.decode())
##### end to add #####
if recv3[:3] != '250':
	print('3 250 reply not received from server.')

# Send DATA command and print server response. 
data = 'DATA\r\n'
##### begin to add #####
# Send DATA down through clientSocket
clientSocket.send(data.encode())
# Save the received message (from server) to 'recv4''
recv4 = clientSocket.recv(1024)
# Print 'recv4'
print(recv4.decode())
##### end to add #####
if recv4[:3] != '354':
	print('4 354 reply not received from server.')

# Send message data.
clientSocket.send('SUBJECT: Greeting To you!\r\n'.encode())
clientSocket.send('test again'.encode())
clientSocket.send(msg.encode())

# Message ends with a single period.
##### begin to add #####
# Send endmsg down through clientSocket
clientSocket.send(endmsg.encode())
# Save the received message (from server) to 'recv5'
recv5 = clientSocket.recv(1024)
# Print 'recv5'
print( recv5.decode())
##### end to add #####
if recv5[:3] != '250':
	print('5 250 reply not received from server.')

# Send QUIT command and get server response.
quitcommand = 'QUIT\r\n'
##### begin to add #####
# Send quitcommand down through clientSocket
clientSocket.send(quitcommand.encode())
# Save the received message (from server) to 'recv6'
recv6 = clientSocket.recv(1024)
# Print 'recv6'
print(recv6.decode())
##### end to add #####
if recv6[:3] != '221':
	print('6 221 reply not received from server.')

