# Cam.BrianBullis
Utilities for the backend of home surveillance.
MotionEyeOS running on a Raspberry Pi 2 Model B used to monitor a camera feed.

#VisionSwitcher.py
Checks the current time versus the time calcuated in Sun.py to be sunrise and sunset to determine whether your camera should be using day or night vision, thereby calling the appropriate vision script.

# DayVision.py
Activates the IR filter on the Arducam to block infrared light and make the image true color.

# NightVision.py
Deactivates the IR filter on the Arducam to let in infrared light reflected from the infrared floodlight aimed at the camera's subject, creating a night vision view.

#Helper Class - Sun.py
Sun.py was graciously provided by a poster on StackOverflow when I was developing this and becoming frustrated, as MotionEyeOS cannot install any additional Python packages (I originally intended to use Astral.) This class uses some hardcore math to calculate the sunrise/sunset for a given coordinate.
