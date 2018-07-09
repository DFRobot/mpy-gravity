# Servo objects control standard hobby servo motors with 3-wires (ground, power, signal).
# There are 4 positions on the pyboard where these motors can be 
# plugged in: pins X1 through X4 are the signal pins, and next to 
# them are 4 sets of power and ground pins.
# the angle of servo is in range(-90,90)
# external power: 5V
# connect:
#     Sensor    pyb
#     VCC       5V
#     GND       GND
#     data1     X1
#     data2     X2


import pyb
import time

s1=pyb.Servo(1)     # create a servo object on position X1
s2=pyb.Servo(2)     # create a servo object on position X2

while(True):
    s1.angle(0)
    s2.angle(0)
    time.sleep(1)
    s1.angle(90)
    s2.angle(90)
    time.sleep(1)
    s1.angle(0)
    s2.angle(0)
    time.sleep(1)
    s1.angle(-90)
    s2.angle(-90)
    time.sleep(1)

