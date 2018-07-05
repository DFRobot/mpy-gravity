# lm35 is used to measure temperature. 

from pyb import ADC,Pin
import time

adc0=ADC(Pin('X1'))
while True:
  val=adc0.read()
  dat=(val/4096)* 3300/10.24
  print("temp=",dat,"C")
  time.sleep(1)
