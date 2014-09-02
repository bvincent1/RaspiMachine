#!/bin/bash
echo "Switching off the light: $(date)" >> /tmp/RaspiMachine.log
sudo python /home/pi/RaspiMachine/Rotate/ControlServo.py 70
