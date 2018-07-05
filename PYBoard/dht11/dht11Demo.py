# DHT11 is used to measure temperature and humidity. 
# You should to download dht11.py before using dht11Demo.py

import dht11
from pyb import Pin
import time

pin = Pin('X1')
dht = dht11.dht11()
while(1):
  temp,hum = dht.read(pin)
  print("temp : %s, hum : %s" %(temp,hum))
  time.sleep(2)