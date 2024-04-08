import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
comp=14
troyka=13
bits=len(dac)
levels=2**bits
maxVoltage=3.3
GPIO.setup(dac,GPIO.OUT)
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
        print(value,signal,voltage)
except KeyboardInterrupt:
    print('No exceptions')
finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup