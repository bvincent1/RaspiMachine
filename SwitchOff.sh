#!/bin/bash
echo "Switching off the light! $(date)" >> /tmp/RaspiMachine.log
sudo python ~/RaspiMachine/Rotate/ControlServo.py 90
