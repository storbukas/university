#!/usr/bin/python
import socket, sys               # Import socket module

s = socket.socket() #socket.AF_INET, socket.SOCK_STREAM)       # Create a socket object
host =  socket.gethostname() #"192.168.0.200"      # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.send((sys.argv[1]).encode())

s.close                     # Close the socket when done
