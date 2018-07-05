# Control dc motor

from pyb import Timer,Pin
from time import sleep
import time

tim=Timer(4,freq=1000)
tchannel=tim.channel(1, Timer.PWM, pin=Pin("P7"), pulse_width_percent=0)

while(1):
  for motorSpeed in range(0,100,5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep(50)
  for motorSpeed in range(100,0,-5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep(50)
