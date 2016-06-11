import RPi.GPIO as GPIO

def msg():
	print "This is a simple message"

msg()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(2, GPIO.OUT)
GPIO.output(2, False)

print "output setted"