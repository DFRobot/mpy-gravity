# ds18b20 is used to measure temperature. 
# You should to download ds18b20.py before using ds18b20Demo.py


from pyb import Pin
import onewire
import ds18b20
import time

ow = onewire.OneWire(Pin('X1'))   #Init wire
ds=ds18b20.DS18X20(ow)          #create ds18x20 object

while True:
  roms=ds.scan()
  ds.convert_temp()             #convert temperature
  for rom in roms:
    print(ds.read_temp(rom))    #display 
  time.sleep(1)

