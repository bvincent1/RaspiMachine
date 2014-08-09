#!/bin/bash
echo "Switching on the light! $(date)" >> /tmp/RaspiMachine.log
sudo python ~/RaspiMachine/Rotate/ControlServo.py 170