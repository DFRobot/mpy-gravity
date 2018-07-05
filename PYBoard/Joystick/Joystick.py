# Read the amplitude in the X and Y of the Joystick and the value in the Z direction

from pyb import ADC,Pin
import time

x=ADC(Pin('X1'))
y=ADC(Pin('X2'))
z=Pin('X3')

while(1):
  print("x : ",x.read()*100//4096)
  print("y : ",y.read()*100//4096)
  print("z : ",z.value())
  time.sleep(0.5)


