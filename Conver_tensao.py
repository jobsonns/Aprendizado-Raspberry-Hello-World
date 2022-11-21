Programa: Conversor Analogico Digital ADS1115 com Raspberry Pi
import board
import busio
import time
#Inicializa a interface I2C
i2c = busio.I2C(board.SCL, board.SDA)
#Define o tipo de módulo usado, no caso, o ADS1115
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
#Cria o objeto ADC
ads = ADS.ADS1115(i2c)
#Define a leitura da porta analogica 0 do módulo
canal0 = AnalogIn(ads, ADS.P0)
canal1 = AnalogIn(ads, ADS.P1)
#Loop que realiza a leitura da porta analogica
while True:
    #tensaopH = float(input(' Digite o valor digital do pH: '))
    #tensaoTemp: float = float(input('Digite o valor digital da temperatura: '))
    print("----------------------------------------------")
    print(f'valor do sinal digital para o pH é: {canal0.value}')
    print(f'valor em voltagem do pH: {canal0.voltage:,.2f}    ')
    if canal0.value >= 2002.17 and canal0.value <= 25335.5:
        print(f'valor do pH é: {canal0.value*0.0006-1.2013:,.2f}')
    else:
        print("Erro na leitura do Sensor")
    print("----------------------------------------------")
    time.sleep(1)
    print(f'valor do sinal analógigo para temperatura: {canal0.value}')
    print(f'valor em voltagem da temperatura: {canal1.voltage:,.2f}')
    if canal1.value>=0 and canal1.value<=27027.03:
        print(f'valor da Temperatura é: {canal1.value*0.0037-20:,.2f}°')
    else:
        print("Erro na leitura do Sensor")
    print("----------------------------------------------")
    time.sleep(3)