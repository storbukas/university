
import wiringpi2 as wiringpi
from time import *

MUSIC = 18
PWM = 2

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18,2) #sets MUSIC to pwm
wiringpi.pwmWrite(18,0)
wiringpi.pwmWrite(18,901)
sleep(1)
wiringpi.pwmWrite(18,902)
sleep(1)
wiringpi.pwmWrite(18,903)
sleep(1)
wiringpi.pwmWrite(18,904)
sleep(1)
wiringpi.pwmWrite(18,0)

