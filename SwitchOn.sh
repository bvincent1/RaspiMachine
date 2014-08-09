#!/usr/bin/python
now = $date
echo "Switching on the light: $now" >> /tmp/RaspiMachine.log
sudo python /home/pi/RaspiMachine/Rotate/ControlServo.py 170