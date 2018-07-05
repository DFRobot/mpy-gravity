# Calculate the light intensity by reading the adc

from pyb import ADC,Pin
import time

adc=ADC(Pin('P6')) # Must always be "P6".

while True:
  print("light intensity : ",adc.read())
  time.sleep(100)
