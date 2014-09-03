#!/bin/bash
echo "Switching on the light: $(date)" >> /tmp/RaspiMachine.log
sudo python /home/pi/RaspiMachine/Rotate/ControlServo.py 0
