# Detect infrared (IR) of people/ animals in motion
# Hardware : PIRMotionSensor, OpenMV
# connect:
#     PIRMotionSensor   OpenMV
#     VCC               3V3
#     GND               GND
#     data              P0

from pyb import Pin,LED
import time

ir=Pin('P0',Pin.IN)     # Connect sensor to 'P0'
led=LED(1)
while(1):
  state = ir.value()    # Read value of ir
  if(state != 0):
    led.on()
    print("Somebody is in this area!")
  else:
    led.off()
    print("No one!")
  time.sleep(500)
