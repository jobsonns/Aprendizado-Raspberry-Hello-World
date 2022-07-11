
try:
    # checks if you have access to RPi.GPIO, which is available inside RPi
    import RPi.GPIO as GPIO
except:
    # In case of exception, you are executing your script outside of RPi, so import Mock.GPIO
    #import Mock.GPIO as GPIO
    from emulator.EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
print('LED ligado')
GPIO.output(17, GPIO.HIGH)
time.sleep(5)
print( 'LED desligado')
GPIO.output(17, GPIO.LOW)
time.sleep(5)