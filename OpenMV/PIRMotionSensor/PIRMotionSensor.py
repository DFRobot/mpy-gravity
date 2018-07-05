# Detect infrared (IR) of people/ animals in motion

from pyb import Pin,LED
import time

ir=Pin('P0',Pin.IN)
led=LED(1)
while(1):
  state = ir.value()
  if(state != 0):
    led.on()
    print("Somebody is in this area!")
  else:
    led.off()
    print("No one!")
  time.sleep(500)
