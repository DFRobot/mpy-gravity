# Read the amplitude in the X and Y of the Joystick and the value in the Z direction
# OpenMV has only one pin to read ADC, so only one of the values of X or Y can be read


import time
from pyb import ADC,Pin

x = ADC("P6") # Must always be "P6".
#y = ADC("P6") # Must always be "P6".
z = Pin("P0")
while(True):
    # The ADC has 12-bits of resolution for 4096 values.
    print("x : ",x.read())
#    print("y : ",y.read())
    print("z : ",z.value())
    time.sleep(500)
