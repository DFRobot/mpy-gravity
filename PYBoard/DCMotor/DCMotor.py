# Control dc motor

from pyb import Timer,Pin
from time import sleep
import pyb
import time

tim=Timer(5,freq=100)
tchannel=tim.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)

while(1):
  for motorSpeed in range(0,100,5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep_ms(50)
  for motorSpeed in range(100,0,-5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep_ms(50)

