# Code for Alpha Protocol-based LED Signs
# http://www.alpha-american.com/alpha-manuals/M-Protocol.pdf

# Assuming Python is installed run:
# sudo apt-get install python-serial
# sudo apt-get install python-pycurl

# To set up cron so it runs the script at startup:
# http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/?ALLSTEPS

# Import python modules
import serial, pycurl, time, json

# Configure the serial port to 9600,7,E,1
ser = serial.Serial('/dev/ttyUSB0', 9600, bytesize=7, parity='E', stopbits=1, timeout=1)

# Write LED display init hex string
def led_init_hex():
        ser.write(chr(0x00)+chr(0x00)+chr(0x00)+chr(0x00)+chr(0x00)+chr(0x01)+chr(0x5A)+chr(0x30)+chr(0x30)+chr(0x02))

# Write LED display escape hex string
def led_escape_hex():
        ser.write(chr(0x04))

# Beep the LED display
def led_beep():
        led_init_hex()
        ser.write(chr(0x45)+chr(0x28)+chr(0x30))
        led_escape_hex()

# Write a string to the LED display
def led_text(string):
        led_init_hex()
        ser.write(chr(0x41)+chr(0x41)+chr(0x1B)+chr(0x20)+chr(0x61)+string)
        led_escape_hex()

# Generate the Misty Logo graphic and save it to file label B
def led_generate_sphero_logo():
        led_init_hex()
        ser.write(chr(0x49)+"B"+chr(0x30)+chr(0x37)+chr(0x30)+chr(0x37))
        ser.write(chr(0x31)+chr(0x31)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x31)+chr(0x31)+chr(0x0d))
        ser.write(chr(0x31)+chr(0x31)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x31)+chr(0x31)+chr(0x0d))
        ser.write(chr(0x31)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x31)+chr(0x0d))
        ser.write(chr(0x31)+chr(0x30)+chr(0x31)+chr(0x30)+chr(0x31)+chr(0x30)+chr(0x31)+chr(0x0d))
        ser.write(chr(0x31)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x31)+chr(0x0d))
        ser.write(chr(0x31)+chr(0x31)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x31)+chr(0x31)+chr(0x0d))
        ser.write(chr(0x31)+chr(0x31)+chr(0x30)+chr(0x30)+chr(0x30)+chr(0x31)+chr(0x31)+chr(0x0d))
        led_escape_hex()

# Allocate memory for text file with file label A and strings with file labels 1 and 2
def led_allocate_memory():
        led_init_hex()
        ser.write("E$"+"AAU0400FF00"+"BDL07071000"+"1BL00400000"+"2BL00400000"+"3BL00400000"+"4BL00400000"+"5BL00400000")
        led_escape_hex()

# Main code follows
print("Running LED display program...")

led_beep()

led_allocate_memory()
led_generate_sphero_logo()

led_init_hex()
ser.write("AA"+chr(0x1b)+chr(0x20)+chr(0x6F)+chr(0x14)+"B"+"  Misty Robotics")
# ser.write("AA"+"Misty Robotics")
led_escape_hex()