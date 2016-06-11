import RPi.GPIO as GPIO
from gpiozero import LED, Button
from signal import pause

led = LED(02)

def msg():
	print "This is a simple message"

msg()

led.on
print "output setted"