try:
  import RPi.GPIO as GPIO
  import board 
  import adafruit_dht
except:
  from collections import namedtuple
  class GPIO():
    def setmode(x): return None;
    def setup(x,y): return None;
    def output(x,y): return None;
    def input(x): return None;
    BCM = None
    OUT = None
    IN = None
    HIGH = None
    LOW = None
  board = namedtuple('board', ['D14'])(None)
  temperature = namedtuple('temperature', ['temperature', 'humidity'])
  class adafruit_dht():
    def DHT11(x): 
      return temperature(10, 50)

GPIO.setmode(GPIO.BCM)

class Input(object):
  def __init__(self, channel):
    self.channel = channel
    self.prev = 60
    GPIO.setup(channel, GPIO.IN)

  def get_value(self):
    return GPIO.input(self.channel)

class DHT11(Input):
  def __init__(self, channel):
    self.channel = channel
    self.internal = adafruit_dht.DHT11(getattr(board, 'D{}'.format(channel)))

  @property
  def temperature(self):
    temp = None
    s = 0
    while temp is None and s < 2:
      try: 
        temp = self.internal.temperature
        self.prev = temp
      except:
        time.sleep(0.5)
        s += 0.5
    if temp is None:
      temp = self.prev
    return temp

  @property
  def humidity(self):
    return self.internal.humidity
    
  
  