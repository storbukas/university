import wiringpi2 as wiringpi
import sys

if (not len(sys.argv) > 1):
    print ("Must pass argument")
    sys.exit()

action = 0
if (str(sys.argv[1]).lower() == "on"):
    action = 1
elif (str(sys.argv[1]).lower() == "off"):
    action = 0 


wiringpi.wiringPiSetup()
wiringpi.pinMode(1,1)       # sets pin 1 to output
wiringpi.pinMode(2,1)       # sets pin 2 to output
wiringpi.pinMode(3,1)       # sets pin 3 to output

wiringpi.digitalWrite(1,action)  # turn ON pin 1
wiringpi.digitalWrite(2,action)  # turn ON pin 2
wiringpi.digitalWrite(3,action)  # turn ON pin 3


