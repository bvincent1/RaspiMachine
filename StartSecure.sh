#!/bin/bash
echo "Starting RaspiSecure: $(date)" >> /tmp/RaspiMachine.log
cd /home/pi/RaspiMachine/Secure/
python MotionCapture.py &
