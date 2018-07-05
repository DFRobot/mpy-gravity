# lm35 is used to measure temperature.

from pyb import ADC,Pin
import time

adc=ADC(Pin('P6'))# Must always be "P6".
while True:
  val=adc.read()
  temp=(val/4096)* 3300/10.24
  print("temp=",temp,"C")
  time.sleep(1000)
