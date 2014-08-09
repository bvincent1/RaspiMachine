#!/usr/bin/python
now = "$(date)"
echo "Switching off the light: $now" >> /tmp/RaspiMachine.log
sudo python /home/pi/RaspiMachine/Rotate/ControlServo.py 90
