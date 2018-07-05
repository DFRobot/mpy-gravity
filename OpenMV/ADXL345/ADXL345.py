# ADXL345 is suitable for tilt Angle measurement 
# and can be used for static gravity acceleration detection
# connect:
#     ADXL345   pyb
#     VCC       5V/3V3
#     GND       GND
#     CS        5V/3V3
#     SDO       GND
#     SDA       SDA
#     SCL       SCL

from pyb import Pin,I2C
import math
import time
DEVICE = 0x53
TO_READ = 6

buff = bytearray(6)
str = bytearray(512)
regAddress = 0x32
x = 0
y = 0
z = 0
roll = 0.00
pitch = 0.00

#calculate the Roll&Pitch
def RP_calculate(x,y,z):
  x_Buff = x
  y_Buff = y
  z_Buff = z
  roll = math.atan2(y_Buff , z_Buff) * 57.3 
  pitch = math.atan2((- x_Buff) , math.sqrt(y_Buff * y_Buff + z_Buff * z_Buff)) * 57.3
  return roll,pitch 
  

i2c=I2C(2,I2C.MASTER,baudrate=100000) 
#Turning on the ADXL345
i2c.mem_write(0, DEVICE, 0x2D)    
i2c.mem_write(16,DEVICE, 0x2D)
i2c.mem_write(8, DEVICE, 0x2D)

while True:
  buff = i2c.mem_read(TO_READ, DEVICE, regAddress)
  if(buff[1] == 0xfe):
    x = buff[0] - 512
  elif(buff[1] == 0xff):
    x = buff[0] - 256
  else:
    x = buff[1]<<8|buff[0]
  
  if(buff[3] == 0xff):
    y = buff[2] -256
  elif(buff[1] == 0xfe):
    x = buff[2] - 512
  else:
    y = buff[3]<<8|buff[2]
    
  if(buff[5] == 0xff):
    z = buff[4] -256
  elif(buff[5] == 0xfe):
    x = buff[4] - 512
  else:
    z = buff[5]<<8|buff[4]

  #we send the x y z values as a string to the serial port
  print("The acceleration info of x : %s, y : %s, z : %s" %(x,y,z))
  #Roll & Pitch calculate
  roll,pitch = RP_calculate(x,y,z)
  print("Roll : %s" %roll)
  print("Pitch : %s" %pitch)
  time.sleep(500)



