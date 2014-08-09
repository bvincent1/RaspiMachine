#!/usr/bin/python
now = $date
echo "Starting RaspiSecure: $now" >> /tmp/RaspiMachine.log
cd /home/pi/RaspiMachine/Secure/
python MotionCapture.py &