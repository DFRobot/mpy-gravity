# Calculate the light intensity by reading the adc
# connect:
#     Sensor    OpenMV
#     VCC       3V3
#     GND       GND
#     data      P6

from pyb import ADC,Pin
import time

adc=ADC(Pin('P6')) # Connect sensor to 'P6', must always be "P6".

while True:
  print("light intensity : ",adc.read())    # Read light intensity
  time.sleep(100)
