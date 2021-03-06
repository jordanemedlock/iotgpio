try:
  import RPi.GPIO as GPIO
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


GPIO.setmode(GPIO.BCM)

class Output(object):
	def __init__(self, channel):
		self.channel = channel
		GPIO.setup(channel, GPIO.OUT)

	def high(self):
		GPIO.output(self.channel, GPIO.HIGH)

	def low(self):
		GPIO.output(self.channel, GPIO.LOW)

	def set_output(self, output):
		GPIO.output(self.channel, output)

class Relay(Output):
	def on(self):
		super().low()
	def off(self):
		super().high()
	def toggle(self):
		super().set_output(not self.state)

	@property
	def is_on(self):
		return not GPIO.input(self.channel)

