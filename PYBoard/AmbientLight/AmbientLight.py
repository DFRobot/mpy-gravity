# Calculate the light intensity by reading the adc
# connect:
#     Sensor    pyb
#     VCC       3V3
#     GND       GND
#     data      X1


from pyb import ADC,Pin
import time

adc=ADC(Pin('X1'))    # Connect sensor to 'X1'

while True:
  print("light intensity : ",adc.read())    # Read light intensity
  time.sleep(0.1)
