# This example is to get the ambient temperature and object temperature by the I2C bus
# connect I2C
#   BME280    OpenMV
#   VCC       VCC
#   GND       GND
#   SCL       SCL
#   SDA       SDA

from pyb import I2C
import time
_MLX90614_IIC_ADDR   = (0x5A)
_MLX90614_TA         = (0x06)
_MLX90614_TOBJ1      = (0x07)

class MLX90614:
  def __init__(self,i2c,addr=_MLX90614_IIC_ADDR):
    self.addr=addr
    self.i2c=i2c

  def getObjCelsius(self):
    return self.getTemp(_MLX90614_TOBJ1)	#Get celsius temperature of the object

  def getEnvCelsius(self):
    return self.getTemp(_MLX90614_TA)    #Get celsius temperature of the ambient

  def getObjFahrenheit(self):
    return (self.getTemp(_MLX90614_TOBJ1) * 9 / 5) + 32  #Get fahrenheit temperature of the object

  def getEnvFahrenheit(self):
    return (self.getTemp(_MLX90614_TA) * 9 / 5) + 32 #Get fahrenheit temperature of the ambient

  def getTemp(self,reg):
    temp = self.getReg(reg)*0.02-273.15             #Temperature conversion
    return temp

  def getReg(self,reg):
    data = self.i2c.mem_read(3,self.addr,reg)               #Receive DATA
    result = (data[1]<<8) | data[0]
    return result

i2c=I2C(2,I2C.MASTER,baudrate=100000)
ir=MLX90614(i2c)
while True:
  time.sleep(1000)
  print("Object  %s *C"% ir.getObjCelsius())        #print celsius of Object
  print("Object  %s *F"% ir.getObjFahrenheit())     #print fahrenheit of Object
  print("Ambient %s *C"% ir.getEnvCelsius())        #print celsius of Ambient
  print("Ambient %s *F"% ir.getEnvFahrenheit())     #print fahrenheit of Ambient
  print()
