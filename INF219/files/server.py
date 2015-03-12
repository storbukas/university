#!/usr/bin/python           # This is server.py file

import socket, sys, os               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    try:
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        c.send('Thank you for connecting')
        input = c.recv(1024)
        if(str(input).lower() == "on"):
            os.system("sudo python triple-led.py "+ str(input))
            print ("Lights on")
        elif(str(input).lower() == "off"):
            os.system("sudo python triple-led.py "+ str(input))
            print ("Lights off")
        else:
            print ("Nothing happens")
        c.close()                # Close the connection
    except KeyboardInterrupt:
        print ("Bye")
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        sys.exit()
