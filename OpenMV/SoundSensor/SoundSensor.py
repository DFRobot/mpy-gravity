# Detection sound intensity

from pyb import ADC,Pin
import time

adc0=ADC(Pin('P6'))# Must always be "P6".
while True:
  val=adc0.read()
  print(val)
  time.sleep(100)
