import time
import ResetServo

from RPIO import PWM
from sys import argv

import xml.etree.ElementTree as ET

DELAY = 1
PIN = 18

SERVO = PWM.Servo()

def getFreq(target):
	return target * 10 + 500

def setServoAngle(angle):
	if angle > 180 or angle < 0:
		raise Exception("Invalid angle. Has to be between 0 and 180 degrees")
	target = getFreq(angle)
	SERVO.set_servo(PIN, target)
	time.sleep(DELAY)

def setServoXML(angle):
	try	:
		tree = ET.parse(FILE_NAME)
		root = tree.getroot()
	except:
		raise Exception("No servo xml found")

	for servo in root.findall("servo"):
		if servo.get("pin") == PIN:
			servo.set("angle",str(angle))
			servo.set("delay",str(DELAY))

	tree = ET.ElementTree(root)
	tree.write(FILE_NAME)
	

if __name__ == "__main__":
	
	if len(argv) < 3:
		# set servo to new position from command line
		setServoAngle(int(argv[1]))

		# update xml
		setServoXML(int(argv[1]))

	
	elif len(argv) < 4:
		# set pin and servo to new position from command line
		PIN = int(argv[2])
		setServoAngle(int(argv[1]))

		# update xml
		setServoXML(int(argv[1]))
		
	else:
		# set pin and servo to new position from command line
		DELAY = int(argv[3])
		PIN = int(argv[2])
		setServoAngle(int(argv[1]))

		# update xml
		setServoXML(int(argv[1]))

	SERVO.stop_servo(PIN)
