#!/usr/bin/env python

"""
VisionSwitcher.py
Meant to be run through cron to check if day or night vision is needed for the camera system
Brian Bullis - bbullis@mail.rit.edu
"""

try:
    from datetime import *
    from Sun import Sun
    import DayVision
    import NightVision
except:
    print("Error importing.")

# Make a sun
sun = Sun()

# The coordinates of the place to check sunrise and sunset
coords = {'longitude' : 123, 'latitude' : 123} # enter the coords of your camera here

# Calculate times to use in the comparisons for deciding which vision to use - THESE ARE IN UTC
sunriseTime = sun.getSunriseTime(coords)['decimal'] * 3600
sunsetTime = sun.getSunsetTime(coords)['decimal'] * 3600
currentTimeTime = datetime.utcnow()
currentTime = currentTimeTime.hour * 3600 + currentTimeTime.minute * 60 + currentTimeTime.second

# Is it before sunrise?
def beforeSunrise():
    return currentTime < sunriseTime

# Is it after sunrise?
def afterSunrise():
    return currentTime > sunriseTime

# Is it before sunset?
def beforeSunset():
    return currentTime < sunsetTime

# Is it after sunset?
def afterSunset():
    return currentTime > sunsetTime

# If sunrise has passed but sunset has not, day vision should be active
def dayVision():
    return afterSunrise() & beforeSunset()

# If it is before sunrise or after sunset, night vision should be active
def nightVision():
    return beforeSunrise() | afterSunset()

if __name__ == '__main__':
    # Call the DayVision script to make it day vision
    if dayVision():
        DayVision.main()
        exit(1)
    # Call the NightVision script to make it night vision
    if nightVision():
        NightVision.main()
        exit(1)
    # What else?
    else:
        exit(0)