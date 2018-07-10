# DHT11 is used to measure temperature and humidity. 
# You should to download dht11.py before using dht11Demo.py
# Hardware : DHT11, PYBoard
# connect:
#     DHT11     PYBoard
#     VCC       3V3
#     GND       GND
#     data      X1

import dht11
from pyb import Pin
import time

pin = Pin('X1')       # Connect sensor to 'X1'
dht = dht11.dht11()
while(1):
  temp,hum = dht.read(pin)      # Read temperature and humidity
  print("temp : %s, hum : %s" %(temp,hum))
  time.sleep(2)