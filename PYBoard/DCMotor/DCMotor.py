# Control dc motor
# Hardware : DCMotor, PYBoard
# connect:
#     DCMotor   PYBoard
#     VCC       3V3
#     GND       GND
#     data      X1

from pyb import Timer,Pin
from time import sleep
import pyb
import time

tim=Timer(5,freq=1000)
tchannel=tim.channel(1, pyb.Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)   # Control PWM output

# Control the motor by setting the duty of PWM
while(1):
  for motorSpeed in range(0,100,5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep_ms(50)
  for motorSpeed in range(100,0,-5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep_ms(50)

