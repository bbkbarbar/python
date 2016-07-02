from __future__ import division
import time
import argparse

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(600)

# Parse arguments
parser = argparse.ArgumentParser('RGB test')
parser.add_argument("-r","--red", type=int, help="red", default = 0)
parser.add_argument("-g","--green", type=int, help="green", default = 0)
parser.add_argument("-b","--blue", type=int, help="blue", default = 0)
parser.add_argument("-x", "--hex", type=str, help="RGB color in hex string", default = "  ")
parser.add_argument("-c", "--complete", type=str, help="all color component in one", default = "  ")
args = parser.parse_args()

allComponent = args.complete

#hexStr = args.hex
#if hexStr[1] == "x":
#	print "got a hex color: " + hexStr
#	data = hexStr[2:]
#	print "Data: |" + data + "|"

# Store values for each color-channel
if allComponent[0] == "a":
	red   = int(allComponent[1:4])
	green = int(allComponent[5:8])
	blue  = int(allComponent[8:10])
else:
	red   = args.red
	green = args.green
	blue  = args.blue

# Set PWM outputs
pwm.set_pwm(0, 0, red)
pwm.set_pwm(1, 0, green)
pwm.set_pwm(2, 0, blue)
#pwm.set_pwm(channel, 0, value)
    