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

from abc import *
import time
import os
import glob

GPIO.setmode(GPIO.BCM)

class Input(object):
  def __init__(self, value=None):
    self.value = value

  def get_value(self):
    return self.value

class GPIOInput(Input):
  def __init__(self, channel, value=None):
    super().__init__(value=value)
    self.channel = channel
    self.prev = 60
    GPIO.setup(channel, GPIO.IN)

  def get_value(self):
    self.value = GPIO.input(self.channel)
    return super().get_value()

class Thermometer(metaclass=ABCMeta):
  @property
  @abstractproperty
  def celcius(self):
    pass


  @property
  def fahrenheit(self):
    return self.celcius * 9.0 / 5.0 + 32
  


class DHT11(Thermometer, Input):
  def __init__(self, channel, value=None):
    super().__init__(value=value)
    self.channel = channel
    self.internal = adafruit_dht.DHT11(getattr(board, 'D{}'.format(channel)))

  def get_value(self):
    self.value = (self.internal.temperature, self.internal.humidity)
    return super().get_value()


  @property
  def temperature(self):
    return self.get_value[0]

  @property
  def humidity(self):
    return self.get_value[1]

  @property
  def celcius(self):
    return self.temperature

class DS18B20(Thermometer, Input):
  def __init__(self, value=None):
    super().__init__(value=value)
    base_dir = '/sys/bus/w1/devices/28*'
    device_folder = glob.glob(base_dir)
    self.device_file = device_folder + '/w1_slave'
  
  def read_lines(self):
    with open(self.device_file, 'r') as fp:
      lines = fp.readlines()
    return lines

  def read_temp(self):
    timeout = 5
    wait = 0.2
    lines = self.read_lines()
    while lines[0].strip()[-3:] != 'YES' and timeout > 0:
      time.sleep(wait)
      timeout -= wait
      lines = self.read_lines()

    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp = float(temp_string) / 1000.0
      return temp
    else:
      raise ValueError('Was unable to get temperature')

  def get_value(self):
    self.value = self.read_temp()
    return super().get_value()

  @property
  def celcius(self):
    return self.get_value()
  

  

    
  
  