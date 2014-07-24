import RPi.GPIO as gpio
import time
from sys import argv

pin = 18
refresh_period = 1

def resetPosition():
	for i in range(1, 100):
		gpio.output(pin, False)
		time.sleep(1.5/1000)
		gpio.output(pin, True)
		time.sleep(refresh_period)

def rotateClockwise():
	for i in range(1, 100):
		gpio.output(pin, False)
		time.sleep(1/1000)
		gpio.output(pin, True)
		time.sleep(refresh_period)


def rotateCounterwise():
        for i in range(1, 100):
		gpio.output(pin, False)
                time.sleep(2/1000)
                gpio.output(pin, True)
                time.sleep(refresh_period)


if __name__ == "__main__":
	gpio.setmode(gpio.BCM)
	gpio.setup(pin, gpio.OUT)
	gpio.setwarnings(False)
	pwm = gpio.PWM(18, 100)
	pwm.start(5)

	if len(argv) > 1:
		angle = float(argv[1])
		target = angle / 10.0 + 2.5
		
		pwm.ChangeDutyCycle(target)
	else:
		while True:
			i = 0
			for i in range(5):
				pwm.ChangeDutyCycle(2.5)
				time.sleep(refresh_period)

			i = 0
			for i in range(5):
				pwm.ChangeDutyCycle(20.5)
				time.sleep(refresh_period)
