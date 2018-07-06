# BME280 can measure temperature, humidity and air pressure and can be
# applied to environmental monitoring
# connect I2C
#   BME280    PYBoard
#   VCC       VCC
#   GND       GND
#   SCL       SCL
#   SDA       SDA
#
# connect SPI
#   BME280    PYBoard
#   VCC       VCC
#   GND       GND
#   MOSI      P0
#   MISO      P1
#   SCLK      P2
#   CS        P3

from pyb import Pin,I2C
import pyb,time
import bme280

i2c=pyb.I2C(2,pyb.I2C.MASTER,baudrate=100000)
bmp=BME280_I2C(i2c)
#spi = pyb.SPI(2, pyb.SPI.MASTER, baudrate=100000, polarity=0, phase=0)
#cs  = Pin("P3", Pin.OUT_OD)
#bmp = BME280_SPI(spi,cs)

while True:
  print("Temp : %s *C" %bmp.getTemp())
  print("Pres : %s Pa" %bmp.getPress())
  print("Alti : %s m"  %bmp.getAltitude())
  print("Humi : %s  "  %bmp.getHumidity())
  print("")
  time.sleep(1000)