import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20, GPIO.IN)
if GPIO.input(20)==1:
    GPIO.output(16,1)
else:
    GPIO.output(16,0)