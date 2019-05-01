offsetI = 0
filteredI = 0
sqI = sumI = 0
int16_t sampleI
Irms = 0

def raiz(fg):
  n = fg / 2.0
  lstX = 0.0
  while (n != lstX):
    lstX = n
    n = (n + fg / n) / 2.0
  
  return n

def calcIrms(amostra, pino_sensor):
  multiplier = 0.125
  
  n = 0
  while (n < amostra):
    sampleI = analogRead(pino_sensor)

    offsetI = (offsetI + (sampleI-offsetI)/1024)
    filteredI = sampleI - offsetI

    sqI = filteredI * filteredI

    sumI += sqI
	n += 1
  
  Irms = raiz(sumI / amostra)*multiplier
  //Reset accumulators
  sumI = 0    
  return Irms
