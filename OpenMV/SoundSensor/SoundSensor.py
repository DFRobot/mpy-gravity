# Detection sound intensity
# connect:
#     Sensor    OpenMV
#     VCC       3V3
#     GND       GND
#     data      P6

from pyb import ADC,Pin
import time

adc0=ADC(Pin('P6'))   # Connect sensor to 'P6', Must always be "P6".
while True:
  val=adc0.read()     # Read data
  print(val)
  time.sleep(100)
