import RPi.GPIO as GPIO
import time

pin = 18
refresh_period = 20/1000

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, True)

while True:
    for i in range(1, 100):
        GPIO.output(pin, False)
        time.sleep(1.5/1000)
        GPIO.output(pin, True)
        time.sleep(refresh_period)
