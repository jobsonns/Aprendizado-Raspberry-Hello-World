from emulator.EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import time

# Variables

delay = 0.0015
steps = 30

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Enable pins for IN1-4 to control step sequence

coil_A_1_pin = 13
coil_A_2_pin = 5
coil_B_1_pin = 23
coil_B_2_pin = 24

# Set pin states

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Function for step sequence

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)




clk = 17
dt = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
clkLastState = GPIO.input(clk)
try:
        while True:
                clkState = GPIO.input(clk)
                if clkState != clkLastState:
                        dtState = GPIO.input(dt)
                        if dtState != clkState:
                                counter += 1
                                for i in range(0, steps*counter):
                                    setStep(1,0,1,0)
                                    time.sleep(delay)
                                    setStep(0,1,1,0)
                                    time.sleep(delay)
                                    setStep(0,1,0,1)
                                    time.sleep(delay)
                                    setStep(1,0,0,1)
                                    time.sleep(delay)

                        else:
                                counter -= 1
                        print (counter)
                        #                clkLastState = clkState
               #sleep(0.01)



finally:
        GPIO.cleanup()