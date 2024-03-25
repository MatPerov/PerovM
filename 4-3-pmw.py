import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
p=GPIO.PWM(24,1000)
p.start(0)
try:
    while True:
        dutycecle=int(input())
        p.start(dutycecle)
        GPIO.output(24,1)
        t.sleep(5)
        p.stop()
finally:
    GPIO.cleanup