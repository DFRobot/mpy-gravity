# Calculate the light intensity by reading the adc

from pyb import ADC,Pin
import time

adc=ADC(Pin('X1'))

while True:
  print("light intensity : ",adc.read())
  time.sleep(0.1)
