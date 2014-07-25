import time

from RPIO import PWM
from sys import argv

PIN = 18
DELAY = 1
SERVO = PWM.Servo()

def getFreq(target):
	return target * 10 + 500

def setServoAngle(angle):
	if angle > 180 or angle < 0:
		raise Exception("Invalid angle. Has to be between 0 and 180 degrees")
	target = getFreq(angle)
	SERVO.set_servo(PIN, target)
	time.sleep(DELAY)

if __name__ == "__main__":
	
	if len(argv) > 1:
		# set servo to new position from command line
		setServoAngle(int(argv[1]))

	
	elif len(argv) > 2:
		# set delay and servo to new position from command line
		DELAY = iny(argv[2])		
		setServoAngle(int(argv[1]))

	SERVO.stop_servo(18)