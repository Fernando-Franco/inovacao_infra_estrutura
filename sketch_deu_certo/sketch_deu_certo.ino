//Programa : Medidor de energia elétrica com Arduino e SCT-013
//Autor : FILIPEFLOP
 
//Baseado no programa exemplo da biblioteca EmonLib
 
//Carrega as bibliotecas
#include <Wire.h>
#include "EmonLib.h" 
#include <LiquidCrystal_I2C.h>
 
EnergyMonitor emon1;
LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7,3, POSITIVE);
 
//Tensao da rede eletrica
int rede = 110.0;
 
//Pino do sensor SCT
int pino_sct = A0;
 
void setup() 
{
  lcd.begin(16, 2);
  lcd.clear();
  Serial.begin(9600);   
  //Pino, calibracao - Cur Const= Ratio/BurdenR. 1800/62 = 29. 
  emon1.current(pino_sct, 30);
  //Informacoes iniciais display
  lcd.setCursor(0,0);
  lcd.print("Corr.(A):");
  lcd.setCursor(0,1);
  lcd.print("Pot. (W):");
} 
  
void loop() 
{ 
  //Calcula a corrente  
  double Irms = emon1.calcIrms(1480);
  //Mostra o valor da corrente
  Serial.print("Corrente : ");
  Serial.print(Irms); // Irms
  lcd.setCursor(10,0);
  lcd.print(Irms);
   
  //Calcula e mostra o valor da potencia
  Serial.print(" Potencia : ");
  Serial.println(Irms*rede);
  lcd.setCursor(10,1);
  lcd.print("      ");
  lcd.setCursor(10,1);
  lcd.print(Irms*rede,1);         // Irms
  lcd.home();
  delay(2000);
}
