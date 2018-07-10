# Servo Control Example
# This example shows how to use your OpenMV Cam to control servos.
# Hardware : Servo, OpenMV
# connect:
#     Servo    OpenMV
#     VCC       5V
#     GND       GND
#     data1     P7
#     data2     P8

import time
from pyb import Servo,Pin

s1 = Servo(1) # P7
s2 = Servo(2) # P8

while(True):
    s1.angle(0)
    s2.angle(0)
    time.sleep(1000)
    s1.angle(90)
    s2.angle(90)
    time.sleep(1000)
    s1.angle(0)
    s2.angle(0)
    time.sleep(1000)
    s1.angle(-90)
    s2.angle(-90)
    time.sleep(1000)
