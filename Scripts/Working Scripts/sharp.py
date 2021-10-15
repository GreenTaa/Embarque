import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)


i = GPIO.input(24)
if i == 0:
    state = "Exist"
    #print(state)
    time.sleep(0.1)
else:
    state = "nothing" 
    time.sleep(0.1)
print(state)
#return(state)

    