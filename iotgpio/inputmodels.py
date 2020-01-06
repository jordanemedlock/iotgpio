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
  class adafruit_dht():
    def DHT11(x): 
      return namedtuple('temperature', ['temperature', 'humidity'])(10, 50)

GPIO.setmode(GPIO.BCM)

class Input(object):
  def __init__(self, channel):
    self.channel = channel
    GPIO.setup(channel, GPIO.IN)

  def get_value(self):
    return GPIO.input(self.channel)

class DHT11(Input):
  def __init__(self, channel):
    self.channel = channel
    self.internal = adafruit_dht.DHT11(getattr(board, 'D{}'.format(channel)))

  @property
  def temperature(self):
    return self.internal.temperature

  @property
  def humidity(self):
    return self.internal.humidity
    
  
  