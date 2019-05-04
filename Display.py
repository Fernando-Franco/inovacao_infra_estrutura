from time import sleep
from LCD import CharLCD

def show(voltagem, potencia):
    lcd = CharLCD(rs=1, en=3, d4=15, d5=13, d6=12, d7=14, cols=16, rows=2)
    voltagem = str(voltagem)
    potencia = str(potencia)
    lcd.clear()
    lcd.message('Voltagem: ' + voltagem, 1)
    lcd.set_line(1)
    lcd.message('Potencia: ' + potencia, 1)
    sleep(1)

def alarm(voltagem, potencia):
    lcd = CharLCD(rs=1, en=3, d4=15, d5=13, d6=12, d7=14, cols=16, rows=2)
    voltagem = str(voltagem)
    potencia = str(potencia)
    lcd.clear()
    lcd.message('TA PEGANDO FOGO BIXO' , 2)
    sleep(0.5)
    lcd.clear()
    lcd.message('Voltagem: ' + voltagem, 1)
    lcd.set_line(1)
    lcd.message('Potencia: ' + potencia, 1)
    sleep(1)


    