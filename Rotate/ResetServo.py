import time
import ControlServo
import xml.etree.ElementTree as ET

from sys import argv


FILE_NAME = 'servo.xml'

"""
<data>
<servo pin=18 angle=0 delay=1/>
<servo pin=23 angle=0 delay=1/>
</data>
"""

def getPosition():
	try	:
		tree = ET.parse(FILE_NAME)
		root = tree.getroot()
	except as e:
		raise Exception("No servo xml found")
	
	pos = []
	for servo in root.findall("servo"):
		pos.append(int(servo.get("angle")), [int(servo.get("pin")), int(servo.get("delay"))])


	# [[angle, pin, delay], [,]]
	return 


if __name__ == "__main__":
	pos_list = getPosition()
	print("Position:" + pos_list)
	for servo in pos_list:
		ControlServo.PIN = servo[1]
		ControlServo.DELAY = servo[2]
		ControlServo.setServoAngle(int(servo[0]))
