#!/usr/bin/env python

"""
DayVision.py
Turn on the IR filter on the Arducam being used for cam.brianbullis.com
Deactivates night vision
Brian Bullis - bbullis@mail.rit.edu
"""

try:
    import RPi.GPIO as G
except:
    print("Error importing RPi.GPIO! Probably need sudo.")

def main():
    # Set warnings to off to quiet the warning that the channel is in use
    G.setwarnings(False)

    # Set pin numbering to Broadcom SOC for Raspberry Pi
    G.setmode(G.BCM)

    # Camera LED is GPIO 32
    CAMLED = 32

    # Set up GPIO to output for the Camera LED
    G.setup(CAMLED, G.OUT, initial=False)

    # Output True to the Camera LED, turning on the IR filter
    G.output(CAMLED,G.HIGH)

if __name__ == '__main__':
    main()