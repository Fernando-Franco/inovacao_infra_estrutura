from import EmonLib.h

EmonLib.EnergyMonitor.current(D0, 111.1) # Corrente: pino de entrada, calibração.

while True:
    Amper = EmonLib.EnergyMonitor.calcIrms(1480)  #Calcular somente Irms
    print(Amper*230.0) #Potência aparente 
    print(Amper) #Irms
