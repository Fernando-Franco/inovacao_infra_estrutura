from math_energy import *

SCT = D1
Volt = 230.0

while True:
    Amper = calcIrms(1480, SCT)  #Calcular somente Irms
    print(Amper*Volt) #Potência aparente 
    print(Amper) #Irms
