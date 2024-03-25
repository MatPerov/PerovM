import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(dac,GPIO.OUT)
a=float(input())
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    while True:
        for i in range(256):
            GPIO.output(dac,decimal2binary(i))
            t.sleep(a)
        for i in range(255,-1,-1):
            GPIO.output(dac,decimal2binary(i))
            t.sleep(a)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup