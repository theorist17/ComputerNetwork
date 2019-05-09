from socket import *

# Message to send
msg = '\r\n I love Konkuk University'
endmsg = '\r\n.\r\n'

# Choose your mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'


##### begin to add #####
# Create a TCP socket called clientSocket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind(('localhost', 50000))
# Connect to the mailserver with port number 587 (Port number may change according to the mail server)
clientSocket.connect((mailserver, 53))
# Save the received message (from server) to 'recv'
recv = clientSocket.recv(1024)
# Print recv
print(recv)
##### end to add #####
if recv[:3] != '220':
	print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO gmail.com\r\n'
##### begin to add #####
# Send heloCommand down through clientSocket
# Save the received message (from server) to 'recv1'
# Print 'recv1'
##### end to add #####
if recv1[:3] != '250':
	print('250 reply not received from server.')
	
# Send MAIL FROM command and print server response.
mailfrom = 'MAIL FROM: <alice@gmail.com>\r\n'
##### begin to add #####
# Send mailfrom down through clientSocket
# Save the received message (from server) to 'recv2'
# Print 'recv2'
##### end to add #####
if recv2[:3] != '250':
	print('250 reply not received from server.')


# Send RCPT TO command and print server response. 
rcptto = 'RCPT TO: <bob@yahoo.com>\r\n'
##### begin to add #####
# Send rcptto down through clientSocket
# Save the received message (from server) to 'recv3'
# Print 'recv3'
##### end to add #####
if recv3[:3] != '250':
	print('250 reply not received from server.')

# Send DATA command and print server response. 
data = 'DATA\r\n'
##### begin to add #####
# Send DATA down through clientSocket
# Save the received message (from server) to 'recv4'
# Print 'recv4'
##### end to add #####
if recv4[:3] != '354':
	print('354 reply not received from server.')

# Send message data.
clientSocket.send('SUBJECT: Greeting To you!\r\n')
clientSocket.send('test again')
clientSocket.send(msg)

# Message ends with a single period.
##### begin to add #####
# Send endmsg down through clientSocket
# Save the received message (from server) to 'recv5'
# Print 'recv5'
##### end to add #####
if recv5[:3] != '250':
	print('250 reply not received from server.')

# Send QUIT command and get server response.
quitcommand = 'QUIT\r\n'
##### begin to add #####
# Send quitcommand down through clientSocket
# Save the received message (from server) to 'recv6'
# Print 'recv6'
##### end to add #####
if recv6[:3] != '221':
	print('221 reply not received from server.')

