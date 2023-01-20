import os

def find_arduino():
    # List all connected devices
    devices = os.popen("ls /dev/").read().split("\n")

    # Iterate over devices and check if it is an arduino
    for device in devices:
        if "ttyACM" in device:
            return "/dev/" + device

arduino_port = find_arduino()
if arduino_port:
    print(arduino_port)
else:
    print("Arduino not found.")
