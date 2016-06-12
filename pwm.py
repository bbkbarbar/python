import RPi.GPIO as GPIO ## Import GPIO library
import argparse

GPIO.setwarnings(False)

def msg(pin, state):
	print "Pin: " + str(pin) + " State: " + str((value*100)/1024) + "%"

def getBool(val):
	if val == 0:
		return False
	else:
		return True

def main():
	parser = argparse.ArgumentParser(' ')
	parser.add_argument("-p","--pin", type=int, help="Output pin", default = 3)

	args = parser.parse_args()

	pin = args.pin

	GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

	GPIO.setup(3, GPIO.PWM) 

	p = GPIO.PWM(pin, 0.5)
	#p = GPIO.PWM(channel, frequency)
	p.start(1)

if __name__ == "__main__":
	main()