import RPi.GPIO as GPIO
import time as t
import matplotlib.pyplot as plt

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
    data=[0]
    Time_begin = t.time()
    GPIO.output(troyka,1)
    flag=True
    timearr=[]
    while flag:
        value=0
        for i in range(bits-1,-1,-1):
            value+=2**i
            signal=adc(value)
            t.sleep(0.005)
            compValue=GPIO.input(comp)
            voltage=value/levels*maxVoltage
            if compValue==1:
                value-=2**i
        data.append(value)
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
        if value>=0.60*256:
            Time_end=t.time()
            flag=False
    GPIO.output(troyka,0)
    expTime=Time_end-Time_begin
    o=0
    while o<expTime and len(timearr)!=len(data):
        o+=expTime/len(data)
        timearr.append(o)
    plt.plot(timearr,data)
    plt.show()
    data_str=[str(item) for item in data]
    with open("data.txt","w") as f:
        f.write("\n".join(data_str))
    with open("settings.txt","w") as f:
        f.write(str(1/(expTime/len(data))))
        f.write("\n"+str(3.3/2**8))
    print('Время эксперимента',expTime)
    print('Период',expTime/len(data))
    print('Частота',1/expTime/len(data))
    print('Шаг квантования',str(3.3/2**8))
except KeyboardInterrupt:
    print('No exceptions')
finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.output(leds,0)
    GPIO.cleanup