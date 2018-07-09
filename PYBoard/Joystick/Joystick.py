# Read the amplitude in the X and Y of the Joystick and the value in the Z direction
# connect:
#     Sensor    pyb
#     VCC       3V3
#     GND       GND
#     x_data    X1
#     y_data    X2
#     z_data    X3

from pyb import ADC,Pin
import time

x=ADC(Pin('X1'))    # Connect to 'X1'
y=ADC(Pin('X2'))    # Connect to 'X2'
z=Pin('X3')         # Connect to 'X3'

while(1):
  print("x : ",x.read()*100//4096)    # Read the amplitude in the X
  print("y : ",y.read()*100//4096)    # Read the amplitude in the Y
  print("z : ",z.value())             # Read Z value
  time.sleep(0.5)


