import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 14
#instance = dht11.DHT11(pin=04)
instance = dht11.DHT11(pin=26)
i = 0
while (i<3):
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("T:" + str(result.temperature) + " H:" + str(result.humidity))

    i = i+1
    time.sleep(1)
