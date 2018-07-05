import time
from pyb import Pin

class dht11:
  def __init__(self):
    pass
  
  def read(self,pin):
    bits = bytearray(5)
    cnt = 7
    idx = 0

    # EMPTY BUFFER
    for i in range(0,5):
      bits[i] = 0

    pin.init(Pin.OUT)
    pin.value(0)
    time.sleep_ms(20)
    pin.value(1)
    pin.init(Pin.IN)
    time.sleep_us(40)

    loopCnt = 10000
    while(pin.value() == 0):
      loopCnt -= 1
      if (loopCnt == 0):
        return -1,-1

    loopCnt = 10000
    while(pin.value() == 1):
      loopCnt -= 1
      if (loopCnt == 0):
        return -1,-1

    for i in range(0,40):
      loopCnt = 10000
      while(pin.value() == 0):
        loopCnt -= 1
        if (loopCnt == 0):
          return -1,-1

      t = time.ticks_us()#############

      loopCnt = 10000
      while(pin.value() == 1):
        loopCnt -= 1
        if (loopCnt == 0):
          return -1,-1

      if ((time.ticks_us() - t) > 40):
        bits[idx] |= (1 << cnt)
      if (cnt == 0):   # next byte?
        cnt = 7    # restart at MSB
        idx+=1     # next byte!
      else:
        cnt-=1

    self.humidity=bits[0]*10+bits[1]
    if(bits[3]&0X80): #negative self.temperature
      self.temperature = 0-(bits[2]*10+((bits[3]&0x7F)))
    else:   #positive self.temperature
      self.temperature = bits[2]*10+bits[3]
    #self.temperature range：-20℃~60℃，self.humidity range:5％RH~95％RH
    if(self.humidity>950):
      self.humidity=950
    if(self.humidity<50):
      self.humidity=50
    if(self.temperature>600):
      self.temperature=600
    if(self.temperature<-200):
      self.temperature = -200
    self.temperature = self.temperature/10 #convert to the real self.temperature value
    self.humidity = self.humidity/10  #convert to the real self.humidity value

    sum = bits[0]+bits[1]+bits[2]+bits[3]
    if (bits[4] != sum):
      return -1,-1
    return self.temperature,self.humidity

