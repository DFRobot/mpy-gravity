# lm35 is used to measure temperature. 
# connect:
#     Sensor    pyb
#     VCC       3V3
#     GND       GND
#     data      X1

from pyb import ADC,Pin
import time

adc0=ADC(Pin('X1'))   # Connect sensor to 'X1'
while True:
  val=adc0.read()     # Read data
  dat=(val/4096)* 3300/10.24    # Calculate the temperature
  print("temp=",dat,"C")
  time.sleep(1)
