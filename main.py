from math_energy import *

Pino_SCT = D1
rede = 230.0

while True:
    Amper = calcIrms(1480, Pino_SCT)  #Calcular corrente
    print(Amper*rede) #Potência aparente 
    print(Amper) #Irms
