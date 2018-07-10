# Detect infrared (IR) of people/ animals in motion
# Hardware : PIRMotionSensor, PYBoard 
# connect:
#     PIRMotionSensor   PYBoard
#     VCC               3V3
#     GND               GND
#     data              X1

from pyb import Pin,LED
import time

ir=Pin('X1',Pin.IN)     # Connect sensor to 'X1'
led=LED(1)
while(1):
  state = ir.value()    # Read value of ir
  if(state != 0):
    led.on()
    print("Somebody is in this area!")
  else:
    led.off()
    print("No one!")
  time.sleep(0.5)
