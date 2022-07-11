from emulator.EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import time 

#ini1 = 24
#ini2 = 23
#en = 25


GPIO.setmode(GPIO.BCM )
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
#GPIO.setup(25, GPIO.OUT)
GPIO.output(24, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
#P = GPIO.PWM(25, 1000)
#P.start(25)
while(1):
    print('Funcionou mesmo!!!')
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    time.sleep(5)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(5)
    