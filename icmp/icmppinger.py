from socket import *
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8
def checksum(str):
	csum = 0
	countTo = (len(str) / 2) * 2
	count = 0
	while count < countTo:
		thisVal = ord(str[count+1]) * 256 + ord(str[count])
		csum = csum + thisVal
		csum = csum & 0xffffffffL
		count = count + 2
	if countTo < len(str):
		csum = csum + ord(str[len(str) - 1])
		csum = csum & 0xffffffffL
	csum = (csum >> 16) + (csum & 0xffff)
	csum = csum + (csum >> 16)
	answer = ~csum
	answer = answer & 0xffff
	answer = answer >> 8 | (answer << 8 & 0xff00)
	return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
	timeLeft = timeout
	#print mySocket, ID, timeout, destAddr
	while 1:
		startedSelect = time.time()
		whatReady = select.select([mySocket], [], [], timeLeft)
		howLongInSelect = (time.time() - startedSelect)
		if whatReady[0] == []: # Timeout
			return "Request timed out."
		timeReceived = time.time()
		recPacket, addr = mySocket.recvfrom(1024)
#Fill in start
#Fetch the ICMP header from the IP packet recPacket and save it to the variable
#icmpHeader. Note: IP header is 20 bytes and ICMP header is 8 bytes. Example:
#recPacket[0:3] would read the first 4 bytes of the IP packet recPacket
		icmpHeader = recPacket[20:28]
		type, code, checksum, id, sequence = struct.unpack("bbHHh", icmpHeader)
		#print "The header received in the ICMP reply is ",type, code, checksum, id, sequence
		if id == ID:
			return timeReceived - startedSelect
#Fetch TTL from the IP packet recPacket and save it to the variable rawTTL in
#string format. Recall that TTL is in the IP header and it is 1 byte. Note: the function
#struct.unpack(format, data) unpack the binary data string according to the given format
		rawTTL = struct.unpack("b", recPacket[8])
#Fill in end
		rawTTL = int(binascii.hexlify(str(rawTTL)), 16)
		timeLeft = timeLeft - howLongInSelect
		if timeLeft <= 0:
			return "Request timed out. rawTTL"

def sendOnePing(mySocket, destAddr, ID):
	# Header is type (8), code (8), checksum (16), id (16), sequence (16)
	myChecksum = 0
	# Make a dummy header with a 0 checksum.
	# struct -- Interpret strings as packed binary data
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	data = struct.pack("d", time.time())
	# Calculate the checksum on the data and the dummy header.
	myChecksum = checksum(header + data)
	# Get the right checksum, and put in the header
	if sys.platform == 'darwin':
		myChecksum = htons(myChecksum) & 0xffff
	#Convert 16-bit integers from host to network byte order.
	else:
		myChecksum = socket.htons(myChecksum)
	header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
	packet = header + data
	mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str
	#Both LISTS and TUPLES consist of a number of objects
	#which can be referenced by their position number within the object
def doOnePing(destAddr, timeout):
	icmp = getprotobyname("icmp")
	#SOCK_RAW is a powerful socket type. For more details see:
	#http://sock-raw.org/papers/sock_raw
#Fill in start
#Create Socket here. Note: you have to somehow use the variable icmp.
	mySocket = socket(AF_INET, SOCK_RAW, icmp)
#Fill in end
	myID = os.getpid() & 0xFFFF #Return the current process i
	sendOnePing(mySocket, destAddr, myID)
	delay = receiveOnePing(mySocket, myID, timeout, destAddr)

	mySocket.close()
	
	return delay

def ping(host, timeout=1):
	#timeout=1 means: If one second goes by without a reply from the server,
	#the client assumes that either the client's ping or the server's pong is lost
	dest = gethostbyname(host)
	print "Pinging " + dest + " using Python:"
	print ""
	#Send ping requests to a server separated by approximately one second
	while 1 :
		delay = doOnePing(dest, timeout)
		print delay
		time.sleep(1)# one second
	return delay

#ping("www.poly.edu")
#ping("127.0.0.1")
ping("www.google.com")

