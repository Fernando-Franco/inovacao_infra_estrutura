
#include "EmonLib.h"
from math import sqrt

offsetI = 1
SCT_Pino = 0
Calibracao = 0

def current(_SCT_Pino, _Calibracao):
    SCT_Pino = _SCT_Pino # Pino do SCT

    # 100A = 33 - 10A = 6.0606
    Calibracao = _Calibracao
    # Este valor é de calibração, destinado justamente para caso queiramos mudar o valor do resistor
    # de carga. Para descobrir ele, basta dividir o número total de voltas (espiras) 
    # do secundário pelo valor do resistor de carga dimensionado
    
    offsetI = 1

def calcIrms(Amostra):
    SupplyVoltage = 3300
    
    n = sumI = 0
    while n < Amostra:
        sampleI = analogRead(SCT_Pino)

        #Filtro low-pass digital extrai o offset de 2,5 V ou 1,65 V dc,
        #então subtrai isto - o sinal está agora centrado em 0 contagens.
        offsetI = (offsetI + (sampleI-offsetI)/1024)
        filteredI = sampleI - offsetI

        # Corrente do método da raiz quadrada média
        # 1) valores atuais quadrados
        sqI = filteredI * filteredI
        # 2) Soma
        sumI += sqI
        n += 1

    I_RATIO = Calibracao *(SupplyVoltage/1000.0)
    Irms = I_RATIO * sqrt(sumI / Amostra)

    return Irms


