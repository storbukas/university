import wiringpi2 as wiringpi
from time import *

LED = 0
LIMIT = 30.0

TRIG = 7
ECHO = 1

ON = 1
OFF = 0

INPUT = 0
OUTPUT = 1

wiringpi.wiringPiSetup()
wiringpi.pinMode(TRIG,OUTPUT) #sets TRIG to output
wiringpi.pinMode(ECHO,INPUT) #sets ECHO to input
wiringpi.pinMode(LED,OUTPUT)

wiringpi.digitalWrite(TRIG, OFF)

sleep(0.1)

print("Starting measurement....")

def getValue():
    wiringpi.digitalWrite(TRIG, ON)
    sleep(0.00001)
    wiringpi.digitalWrite(TRIG, OFF)

    while (not (wiringpi.digitalRead(ECHO))):
        pass

    start = time()

    while (wiringpi.digitalRead(ECHO)):
        pass

    stop = time()

    return((stop-start)*17000)

def sensor():
    value1 = getValue()
    sleep(0.05)
    value2 = getValue()
    return ((value1 + value2)/2)
   
def main():
    status = False
    previous = False
    while(1):
        status = sensor() < LIMIT
        if(status):
            if(not previous):
                wiringpi.digitalWrite(LED,ON)
                previous = True
            else:
                wiringpi.digitalWrite(LED,OFF)
                previous = False
            
            while(sensor() < LIMIT):
                sleep(0.1)
                pass
        #wiringpi.digitalWrite(LED,ON)
        #else:
            #wiringpi.digitalWrite(LED,OFF)
       
        sleep(0.1)

if __name__ == "__main__":
    main()
