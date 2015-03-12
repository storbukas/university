import wiringpi as wiringpi
from time import sleep

wiringpi.wiringPiSetup()
wiringpi.pinMode(8,0) #sets pin 8 to input
wiringpi.pinMode(0,1) #sets pin 0 to output

while(1):

    if(not wiringpi.digitalRead(8)):
        wiringpi.digitalWrite(0,1) #sets pin 0 to ON

    else:
        wiringpi.digitalWrite(0,0) #sets pin 0 to OFF
 	
    sleep(0.2)

