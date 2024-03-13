import sqlite3
import Adafruit_DHT
import time
from datetime import datetime
import RPi.GPIO as GPIO
import logging

pin = 16
botao = 20
sensor = Adafruit_DHT.DHT11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #.BCM numeração das GPIO /.BOARD numeraçao da placa

GPIO.setup(20, GPIO.IN)

logging.basicConfig(filename='DHT11.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def criarTabela():
    nome_mes = datetime.now().strftime('%B').lower()
    nome_arquivo = f'{nome_mes}.db' #define o nome do arquivo como o mês atual
    conn = sqlite3.connect(nome_arquivo) #conecta no banco com o nome do mês atual(ou cria um se ñ existir)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS temperaturas
                      (id INTEGER PRIMARY KEY, data TEXT, hora TEXT, temperatura INTEGER)''')
    conn.commit()
    conn.close()

def inserirDados(data, hora, temperatura):
    nome_mes = datetime.now().strftime('%B').lower()
    nome_arquivo = f'{nome_mes}.db' #define o nome do arquivo como o mês atual
    conn = sqlite3.connect(nome_arquivo) #conecta no banco com o nome do mês atual(ou cria um se ñ existir)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO temperaturas (data, hora, temperatura) VALUES (?, ?, ?)',(data, hora, temperatura))
    conn.commit()
    conn.close()
    
criarTabela()
       
while True:
    try:
        if GPIO.input(botao) == GPIO.HIGH:
            tempo_inicial = time.time()
            while (time.time() - tempo_inicial) < 1800:  #duração da execução em segundos (30 minutos = 1800)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_date = now.strftime("%d-%m-%Y")
                temperatura = Adafruit_DHT.read_retry(sensor,pin)[1]
                
                inserirDados(current_date, current_time, temperatura)
            
                print('Data:', current_date)
                print('Hora:', current_time)
                print('Temperatura: {0:0.1f}C'.format(temperatura))
                print(" ")
                print("temperatura salva")
                time.sleep(15) #Tempo entre as consultas/leituras
            print("fim da execução.")
            fim = "Fim da execução"
            inserirDados(fim, fim, 0) #Registra um "separador" no banco de dados para facilitar compreensão
    except Exception as e:
        logging.error('Ocorreu um erro: %s', str(e))
