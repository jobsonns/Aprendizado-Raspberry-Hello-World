
from emulator.EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
cont=0
while(cont<10000):
    print('LED ligado')
    print(cont)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.25)
    cont=cont+1
    GPIO.output(17, GPIO.LOW)
    time.sleep(0.25)
