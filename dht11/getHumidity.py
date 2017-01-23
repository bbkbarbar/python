import RPi.GPIO as GPIO
import dht11
import time
import datetime
import argparse


def tryToRead():
	result = instance.read()
	if result.is_valid():
	    return result.humidity
	else:
	    return "-1"

def main():
	parser = argparse.ArgumentParser('GPIO output controller')
	parser.add_argument("-p","--pin", type=int, help="Input pin", default = 7)
	parser.add_argument("-m","--mock", type=int, help="Value to mockReturn", default = -99)

	args = parser.parse_args()
	pin = args.pin
	mockValue = args.mock

	if(pin == -1):
		print "Humidity: " + str(mockValue)
		return;

	if(mockValue == -99):
		print "Humidity: " + str(mockValue)
	else:

		# initialize GPIO
		GPIO.setwarnings(False)
		#GPIO.setmode(GPIO.BCM)
		GPIO.setmode(GPIO.BOARD)
		GPIO.cleanup()


		instance = dht11.DHT11(pin)
		success = 0

		for tryCounter in range(0, 4):
			res = tryToRead()
			if res >= 0:
				success = 1
				print "Humidity: " + str(res)
			time.sleep(1)

		if success == 0:
			print "Humidity: -1"


if __name__ == "__main__":
	main()
