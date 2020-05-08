# rpi_led_sign
LED Display Driver to connect a Raspberry Pi to the Alpha Sign Communications Protocol Type LED Displays

# Code for Alpha Protocol-based LED Signs
# http://www.alpha-american.com/alpha-manuals/M-Protocol.pdf

# Assuming Python is installed run:
sudo apt-get install python-serial
sudo apt-get install python-pycurl

# To set up cron so it runs the script at startup:
# http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/?ALLSTEPS

My setup uses a Raspberry Pi B+, Acroname USB to serial adapter, WiFi Dongle, and an Alpha 215R LED Display.

These displays can be found in a variety of sizes on eBay from small to feet by feet. The same script worked with a 4' x 8' display I tested it on also, you just had to deal with multiple lines.