# BME280 can measure temperature, humidity and air pressure and can be
# applied to environmental monitoring
# BME280 supports the SPI/I2C communication.
# Hardware : BME280, PYBoard
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
#   MOSI      X8
#   MISO      X7
#   SCLK      X6
#   CS        X1

from pyb import Pin,I2C
import pyb,time
import bme280

# BME280 communicates with I2C
i2c=pyb.I2C(1,pyb.I2C.MASTER,baudrate=100000)     
bme=BME280_I2C(i2c)

# BME280 communicates with SPI
#spi = pyb.SPI(1, pyb.SPI.MASTER, baudrate=100000, polarity=0, phase=0)
#cs  = Pin("X1", Pin.OUT_OD)
#bme = BME280_SPI(spi,cs)


# Print data
while True:
  print("Temp : %s *C" %bme.getTemp())
  print("Pres : %s Pa" %bme.getPress())
  print("Alti : %s m"  %bme.getAltitude())
  print("Humi : %s  "  %bme.getHumidity())
  print("")
  time.sleep(1)