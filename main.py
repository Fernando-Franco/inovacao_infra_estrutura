from Display import show, alarm
from math_energy import calcIrms

digital = 0 
led = 0
sensor = 0

rede = 110
maxInput = 0

pinMode(led, OUTPUT)
pinMode(sensor, INPUT_ANALOG)
pinMode(digital, OUTPUT)


while True:

    amper = calcIrms(1480, sensor)  #Calcular corrente
    if amper <= maxInput:
        digitalWrite(led, LOW)
        show(amper, amper*rede)
    else:
        alarm(amper, amper*rede)
        digitalWrite(led, HIGH)

