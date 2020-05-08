#!/bin/sh
# launcher.sh
# navigate to home directory, then execute python script, then back home

cd /
cd home/pi/led_sign
sudo python mini-led-sign.py
cd /