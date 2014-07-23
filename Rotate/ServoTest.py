# Servo Control
import time
import RPi.GPIO as GPIO

while True:
   GPIO.output(pin, GPIO.HIGH)  
   time.sleep(0.0015)  
   GPIO.output(pin, GPIO.LOW)  
   time.sleep(0.0185)