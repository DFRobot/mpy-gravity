# Detection sound intensity

from pyb import ADC,Pin
import time

adc0=ADC(Pin('X1'))
while True:
  val=adc0.read()
  print(val)
  time.sleep(0.1)

