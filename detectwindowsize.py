#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module Has Been Built for the Steam Game 'Realm Grinder'.

Specifically, to locate the and adjust the hardcoded XY coordinates for
different screen sizes.

Laptop Screen Size Directly Correlates to the x, y axis of mouse navigation.
If you are to change your screen dimensions during use of PyAutoGUI the
"FAILSAFE" will NOT WORK.

Creation Date: 20190809
ref: https://stackoverflow.com/a/4152986/1896134

"""
# =============================================================================
from os import getcwd
from os import path

from pyautogui import size
current_local = getcwd()
filename = path.join(current_local, path.basename(__file__))


class DetectWindowSize():
    """Determine Your Settings needed for RG for Screen Size & Location."""

    def __init__(self):
        """Module DetectWindowSize __init__."""
        self.x_cordinate = int(10)
        self.y_cordinate = int(10)
        self.adjustments = int(0)
        self.size = int(0)

    def main(self):
        """SET WindowSize variables."""
        if str(size()) == 'Size(width=1440, height=900)':
            # Laptop Screen.
            self.x_cordinate = int(600)
            self.y_cordinate = int(580)
            self.adjustments = int(0)
            self.size = (1440, 900)
            return
        elif str(size()) == 'Size(width=1920, height=1080)':
            # TV Screen Using Thunderbolt to HDMI.
            self.x_cordinate = int(620)
            self.y_cordinate = int(620)
            self.adjustments = int(60)
            self.size = (1920, 1080)
            return
        else:
            print('No Setting for screen size: {}'.format(size()))
            exit()

    @property
    def windowsize(self):
        """Print WindowSize."""
        return self.size


if __name__ == "__main__":
    print("{} has been called from {}".format(path.basename(__file__),
                                              filename))
    print('Screen Size: ' + str(size()))
    D = DetectWindowSize()
    DetectWindowSize.main(D)
    print('Screen Size: {}'.format(D))
    print("x_cordinate: {}".format(D.x_cordinate))
    print("y_cordinate: {}".format(D.y_cordinate))
    print("adjustments: {}".format(D.adjustments))
    print(D.y_cordinate)
    print(D.adjustments)
