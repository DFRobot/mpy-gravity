# This example is to get the ambient temperature and object temperature by the I2C bus
# connect I2C
#   BME280    PYBoard
#   VCC       VCC
#   GND       GND
#   SCL       SCL
#   SDA       SDA

from pyb import I2C
import time
import MLX90614

i2c=I2C(1,I2C.MASTER,baudrate=100000) 
ir=MLX90614.MLX90614(i2c)
while True:
  time.sleep(1)
  print("Object  %s *C"% ir.getObjCelsius())        #print celsius of Object
  print("Object  %s *F"% ir.getObjFahrenheit())     #print fahrenheit of Object
  print("Ambient %s *C"% ir.getEnvCelsius())        #print celsius of Ambient
  print("Ambient %s *F"% ir.getEnvFahrenheit())     #print fahrenheit of Ambient
  print()
