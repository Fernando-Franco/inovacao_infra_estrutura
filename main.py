import EmonLib.h

Serial.begin(9600)
EmonLib.EnergyMonitor.current(D0, 111.1) # Corrente: pino de entrada, calibração.

while True:
    Amper = EmonLib.EnergyMonitor.calcIrms(1480)  #Calcular somente Irms
    Serial.print(Amper*230.0) #Potência aparente 
    Serial.print(" ")
    Serial.println(Amper) #Irms


