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

import time,math
from pyb import Pin,I2C
import pyb


class BME280():
  def __init__(self):
    self.T1 = self.get2Reg(0x88)
    self.T2 = self.short(self.get2Reg(0x8A))
    self.T3 = self.short(self.get2Reg(0x8C))
    self.P1 = self.get2Reg(0x8E)
    self.P2 = self.short(self.get2Reg(0x90))
    self.P3 = self.short(self.get2Reg(0x92))
    self.P4 = self.short(self.get2Reg(0x94))
    self.P5 = self.short(self.get2Reg(0x96))
    self.P6 = self.short(self.get2Reg(0x98))
    self.P7 = self.short(self.get2Reg(0x9A))
    self.P8 = self.short(self.get2Reg(0x9C))
    self.P9 = self.short(self.get2Reg(0x9E))

    self.H1 = self.getReg(0xa1);
    self.H2 = self.short(self.get2Reg(0xe1))
    self.H3 = self.getReg(0xe3);
    self.H4 = (self.getReg(0xe4) << 4) | (self.getReg(0xe4+1) & 0xF);
    self.H5 = (self.getReg(0xe5+1) << 4) | (self.getReg(0xe5) >> 4);
    self.H6 = self.getReg(0xe7)

    self.setReg(0xF2, 0x05)
    self.setReg(0xF5, 0x0C)
    self.setReg(0xF4, 0x2F)
    
  def short(self, data):
    if data > 32767: return data-65536
    else: return data

  def getTemp(self):
    adc_T = (self.getReg(0xFA)<<12) + (self.getReg(0xFB)<<4) + (self.getReg(0xFC)>>4)
    var1 = (((adc_T>>3)-(self.T1<<1))*self.T2)>>11
    var2 = (((((adc_T>>4)-self.T1)*((adc_T>>4) - self.T1))>>12)*self.T3)>>14
    self.fine = var1+var2
    temp = ((self.fine * 5 + 128) >> 8)/100
    return temp

  def getPress(self):
    var1 = (self.fine>>1) - 64000
    var2 = (((var1>>2) * (var1>>2)) >> 11 ) * self.P6
    var2 = var2 + ((var1*self.P5)<<1)
    var2 = (var2>>2)+(self.P4<<16)
    var1 = (((self.P3*((var1>>2)*(var1>>2))>>13)>>3) + (((self.P2) * var1)>>1))>>18
    var1 = ((32768+var1)*self.P1)>>15
    if var1 == 0:
      return -1
    adc_P = (self.getReg(0xF7)<<12) + (self.getReg(0xF8)<<4) + (self.getReg(0xF9)>>4)
    p=((1048576-adc_P)-(var2>>12))*3125
    if p < 0x80000000:
      p = (p << 1) // var1
    else:
      p = (p // var1) * 2
    var1 = (self.P9 * (((p>>3)*(p>>3))>>13))>>12
    var2 = (((p>>2)) * self.P8)>>13
    pres = p + ((var1 + var2 + self.P7) >> 4)
    return pres


  def getAltitude(self):
    return 44330*(1-(self.getPress()/101325)**(1/5.255))

  def getHumidity(self):
    adc_H = self.get2RegS(0xfd);
    if (adc_H == 0x8000):  # value in case humidity measurement was disabled
      print('get humidity failure')
      return -2
    tmp = self.fine - 76800
    tmp = (((((adc_H << 14) - (self.H4 << 20) - self.H5 * tmp) + 16384) >> 15) * (((((((tmp * self.H6) >> 10)*(((tmp * self.H3) >> 11) + 32768)) >> 10) + 2097152) * self.H2 + 8192) >> 14))
    tmp = tmp - (((((tmp >> 15) * (tmp >> 15)) >> 7) * self.H1) >> 4)
    tmp = 0 if (tmp < 0) else tmp
    tmp = 419430400 if(tmp > 419430400) else tmp
    h = tmp>>12
    return  h / 1024

class BME280_I2C(BME280):
  def __init__(self,i2c):
    self.i2c = i2c
    self.addr = 0x77
    super(BME280_I2C,self).__init__()

  def setReg(self,reg,data):
    self.i2c.mem_write(data,self.addr, reg)

  def getReg(self,reg):
    data = self.i2c.mem_read(1,self.addr,reg)
    return data[0]

  def get2Reg(self,reg):
    data = self.i2c.mem_read(2,self.addr,reg)
    return data[0]+data[1]*256

  def get2RegS(self,reg):
    data = self.i2c.mem_read(2,self.addr,reg)
    return data[1]+data[0]*256

class BME280_SPI(BME280):
  def __init__(self,spi,cs):
    self.spi = spi
    self.cs = cs
    super(BME280_SPI,self).__init__()

  def begin(self):
    print(self.getReg(0xd0))

  def setReg(self,reg,data):
    regAddr = bytearray(1)
    val = bytearray(1)
    regAddr[0] = reg&0x7f
    val[0] = data
    self.cs.low()
    self.spi.write(regAddr)
    self.spi.write(val)
    self.cs.high()

  def getReg(self,reg):
    regAddr = bytearray(1)
    regAddr[0] = reg|0x80
    self.cs.low()
    self.spi.write(regAddr)
    rslt = self.spi.read(1+1)
    self.cs.high()
    return rslt[0]

  def get2Reg(self,reg):
    regAddr = bytearray(1)
    regAddr[0] = reg|0x80
    self.cs.low()
    self.spi.write(regAddr)
    rslt = self.spi.read(2+1)
    self.cs.high()
    return rslt[0]+rslt[1]*256

  def get2RegS(self,reg):
    regAddr = bytearray(1)
    regAddr[0] = reg|0x80
    self.cs.low()
    self.spi.write(regAddr)
    rslt = self.spi.read(2+1)
    self.cs.high()
    return rslt[1]+rslt[0]*256

i2c=pyb.I2C(2,pyb.I2C.MASTER,baudrate=100000)
bme=BME280_I2C(i2c)
#spi = pyb.SPI(2, pyb.SPI.MASTER, baudrate=100000, polarity=0, phase=0)
#cs  = Pin("P3", Pin.OUT_OD)
#bme = BME280_SPI(spi,cs)

while True:
  print("Temp : %s *C" %bme.getTemp())
  print("Pres : %s Pa" %bme.getPress())
  print("Alti : %s m"  %bme.getAltitude())
  print("Humi : %s  "  %bme.getHumidity())
  print("")
  time.sleep(1000)
