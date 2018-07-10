# Control dc motor
# Hardware : DCmotor, OpenMV
# connect:
#     DCmotor    OpenMV
#     VCC       3V3
#     GND       GND
#     data      P7

from pyb import Timer,Pin
from time import sleep
import time

tim=Timer(4,freq=1000)
tchannel=tim.channel(1, Timer.PWM, pin=Pin("P7"), pulse_width_percent=0)  # Control PWM output

# Control the motor by setting the duty of PWM
while(1):
  for motorSpeed in range(0,100,5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep(50)
  for motorSpeed in range(100,0,-5):
    tchannel.pulse_width_percent(motorSpeed)
    time.sleep(50)
