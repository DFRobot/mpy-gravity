# Detection sound intensity
# Hardware : SoundSensor, PYBoard 
# connect:
#     SoundSensor   PYBoard
#     VCC           3V3
#     GND           GND
#     data          X1

from pyb import ADC,Pin
import time

adc0=ADC(Pin('X1'))   # Connect sensor to 'X1'
while True:
  val=adc0.read()     # Read data
  print(val)
  time.sleep(0.1)

