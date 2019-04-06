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

sun = Sun()
coords = {'longitude' : 123, 'latitude' : 123} # enter the coords of your camera here

sunriseTime = sun.getSunriseTime(coords)['decimal'] * 3600
sunsetTime = sun.getSunsetTime(coords)['decimal'] * 3600
currentTimeTime = datetime.utcnow()
currentTime = currentTimeTime.hour * 3600 + currentTimeTime.minute * 60 + currentTimeTime.second

def beforeSunrise():
    return currentTime > sunriseTime

def afterSunrise():
    return currentTime < sunriseTime

def beforeSunset():
    return currentTime > sunsetTime

def afterSunset():
    return currentTime < sunsetTime

def dayVision():
    return afterSunrise() & beforeSunset()

def nightVision():
    return beforeSunrise() | afterSunset()

if __name__ == '__main__':
    if dayVision():
        DayVision.main()
    if nightVision():
        NightVision.main()
    else:
        exit(0)
