import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

dac=[8,11,7,1,0,5,12,6]
leds=[2,3,4,17,27,22,10,9]
comp=14
troyka=13
bits=len(dac)
levels=2**bits
maxVoltage=3.3


GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc(value):
    signal=decimal2binary(value)
    GPIO.output(dac,signal)
    return signal

try:
    while True:
        value=0
        for i in range(bits-1,-1,-1):
            value+=2**i
            signal=adc(value)
            t.sleep(0.0007)
            compValue=GPIO.input(comp)
            voltage=value/levels*maxVoltage
            if compValue==1:
                value-=2**i
        i=0
        n=0
        light=[0 for j in range(bits)]
        lights=[0 for j in range(bits)]
        while value>i:
            i+=32
            light[n]=1
            n+=1
        for i in range(len(light)):
            lights[i]=light[len(light)-1-i]
        print(value,signal,voltage)
        GPIO.output(leds,lights)
except KeyboardInterrupt:
    print('No exceptions')
finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.output(leds,0)
    GPIO.cleanup