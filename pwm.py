import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

#p = GPIO.PWM(3, 0.5)
p = GPIO.PWM(3, 50)
p.ChangeDutyCycle(100)
p.start(1)
raw_input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()