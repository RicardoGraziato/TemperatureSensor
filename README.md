# TemperatureSensor
## Este projeto consiste em um programa em Python para Raspberry Pi integrado com banco de dados SQLite que capta e registra temperaturas (ambiente e de líquidos) via sensores DHT11 e DS18B20.

O programa tem função de captar valores de temperatura de ambiente e de água através de sensores (DHT11 e DS18B20 respectivamente)
e armazenar em um banco de dados SQLite (1 banco por mês, sendo essa troca feita automaticamente). Também serão armazenadas as informações de data/hora
que a temperatura foi captada pelo sensor.

Executando continuamente aguardando um sinal vindo de um botão físico (quando este for pressionado); Ao receber esse sinal (usuário pressionar o botão),
o programa captura a temperatura de 15 em 15 segundos durante 30 minutos (120 temperaturas captadas por execução) e depois volta a aguardar o sinal novamente.

Requer no mínimo 2 GPIOs (um para o botão e outro para um dos sensores). E para o DS18B20 é necessário um resistor ligando o a entrada de dados (cabo amarelo) e o 3.3v (cabo vermelho).

-Instalações:
pip install Adafruit_DHT | (DHT)
pip install w1thermsensor | (DS18B20 - É preciso também abilitar o 1-Wire nas configurações do raspberry. Geralmente a GPIO padrão é a GPIO4 porém pode ser alterada. ).

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

This project consists of a Python program for Raspberry Pi integrated with an SQLite database.

The program's purpose is to capture temperature values from the environment and water using sensors (DHT11 and DS18B20, respectively) and store them in an SQLite database. A new database is created each month, facilitating data organization. Additionally, the date and time information of the temperature capture by the sensor are also recorded.

The program runs continuously, awaiting a signal from a physical button. When the button is pressed by the user, the program starts capturing temperature every 15 seconds for 30 minutes (totaling 120 temperature captures per execution). After this period, the program resumes waiting for the button signal to initiate a new capture.

Requires at least 2 GPIOs (one for the button and one for one of the sensors). And for DS18B20, it's necessary to connect a resistor between the data-input(yellow) and the 3.3V (red).

-Installations:
pip install Adafruit_DHT | (DHT)
pip install w1thermsensor | (DS18B20 - It is also necessary to enable 1-Wire in the Raspberry settings. The default GPIO is usually GPIO4, but it can be changed.).
