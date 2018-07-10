# Read the amplitude in the X and Y of the Joystick and the value in the Z direction
# OpenMV has only one pin to read ADC, so only one of the values of X or Y can be read
# Hardware : Joystick, OpenMV
#     Joystick        OpenMV
#     VCC             3V3
#     GND             GND
#     x_data/y_data   P6
#     z_data          P0

import time
from pyb import ADC,Pin

x = ADC("P6") # Must always be "P6".
#y = ADC("P6") # Must always be "P6".
z = Pin("P0")

# The ADC has 12-bits of resolution for 4096 values.
while(True):
    print("x : ",x.read()*100//4096)      # Read the amplitude in the X
#    print("y : ",y.read()*100//4096)
    print("z : ",z.value())               # Read Z value
    time.sleep(500)
