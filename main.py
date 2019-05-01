import EmonLib.h 

EmonLib.EnergyMonitor emon1

Serial.begin(9600)
emon1.current(D0, 111.1) # Corrente: pino de entrada, calibração.

while True:
    double Amper = emon1.calcIrms(1480)  #Calcular somente Irms
    Serial.print(Amper*230.0) #Potência aparente 
    Serial.print(" ")
    Serial.println(Amper) #Irms


