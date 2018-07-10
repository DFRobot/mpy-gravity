# lm35 is used to measure temperature.
# Hardware : lm35, OpenMV
# connect:
#     lm35      OpenMV
#     VCC       3V3
#     GND       GND
#     data      P6

from pyb import ADC,Pin
import time

adc=ADC(Pin('P6'))  # Must always be "P6".
while True:
  val=adc.read()    # Read data
  temp=(val/4096)* 3300/10.24   # Calculate the temperature
  print("temp=",temp,"C")
  time.sleep(1000)
