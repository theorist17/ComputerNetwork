#!/usr/bin/python3
import sys, time
from socket import *

# Get the server hostname and port as command line arguments
argv = sys.argv                      
host = argv[1]
port = argv[2]
timeout = 1 # in second

##### Begin to add #####
# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second (use settimeout(timeout value) function)
clientSocket.settimeout(timeout)
##### End to add #####

# Command line argument is a string, change the port into integer
port = int(port)  
# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent (this is the ping message)
    data = "Ping " + str(ptime) + " " + time.asctime()
    
    try:
        ##### Begin to add #####
        # Sent time = RTTb (use time() function)
        RTTb = time.time()
        # Send the UDP packet with the ping message
        clientSocket.sendto(data.encode(), (host, port))
        # Receive the server response
        message, address = clientSocket.recvfrom(1024)
        # Received time = RTTa (use time() function)
        RTTa = time.time()
        ##### End to add #####
        
        # Display the server response as an output
        print("Reply from " + address[0] + ": " + message.decode())
        # Round trip time is the difference between sent and received time
        print("RTT: " + str(RTTa - RTTb))
    except Exception as e:
        # Server does not response
        # Assume the packet is lost
        print("Request timed out.")
        continue

##### Begin to add #####
# Close the client socket
clientSocket.close()
##### End to add #####


