import RPi.GPIO as GPIO
import time as t
dac=[8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    value=int(input())
    if value=='q':
        pass
    if type(value)==float:
        print('Нужно целое число')
        pass
    if value<0:
        print("Нужно неотрицательное число")
        pass
    if value>255:
        print("Слишком большое число")
        pass
    if type(value)!=int:
        print('Нужно число')
    GPIO.output(dac,decimal2binary(value))
    t.sleep(1)
    step=1/255
    U=3.3*value*step
    print('Напряжение:',U)
except ValueError:
    print('Нужно число')
    pass
except KeyboardInterrupt as e:
    pass
finally:
    GPIO.output(dac,0)
    GPIO.cleanup
