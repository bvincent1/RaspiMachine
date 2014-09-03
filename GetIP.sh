#!/bin/bash
echo "Starting Getting IP ADDR: $(date)" >> /tmp/RaspiMachine.log
cd /home/pi/RaspiMachine/IpUpdate/
python IpGet.py
