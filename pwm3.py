import time
import RPi.GPIO as GPIO
import argparse

GPIO.setmode(GPIO.BOARD)

def main():

	parser = argparse.ArgumentParser('3ch PWM controller')
	parser.add_argument("-c","--channel", type=int, help="output channel", default = 3)
	parser.add_argument("-v","--value", type=int, help="pwm value (maybe in percentage)")
	parser.add_argument("-f","--freq", type=int, help="pwm frequency", default = 200)

	args = parser.parse_args()
	channel = args.channel
	value = args.value
	freq = args.freq

	if channel == 0:
		p = GPIO.PWM(channel, freq)  
		p.stop()
		GPIO.cleanup()
		
	else:

		#pinRed = 3
		#pinGreen = 5
		#pinBlue = 7

		GPIO.setup(channel, GPIO.OUT)
		#GPIO.setup(pinRed, GPIO.OUT)
		#GPIO.setup(pinGreen, GPIO.OUT)
		#GPIO.setup(pinBlue, GPIO.OUT)

		p = GPIO.PWM(channel, freq)  # channel=pinRed frequency=50Hz
		#chGreen = GPIO.PWM(pinGreen, 200)  # channel=pinRed frequency=50Hz
		#chBlue = GPIO.PWM(pinBlue, 200)  # channel=pinRed frequency=50Hz

		p.start(0)
		p.ChangeDutyCycle(value)

		chRed.stop()
		GPIO.cleanup()


if __name__ == "__main__":
	main()