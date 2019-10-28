#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module Has Been Built for the Steam Game 'Realm Grinder'."""
# Laptop Screen Size Directly Correlates to the x, y axis of mouse navigation.
# =============================================================================
import os
import platform
from pprint import pprint
from random import choice
from random import uniform
from time import strftime

from pyautogui import click
from pyautogui import easeInBounce
from pyautogui import easeInElastic
from pyautogui import easeInOutQuad
from pyautogui import easeInQuad
from pyautogui import easeOutQuad
from pyautogui import moveTo
from pyautogui import size

# from random import randint

# =============================================================================
# MOVE MOUSE COURSOR THIS RUNS FOR EVERY CLICK NOT JUST ONCE
# =============================================================================


def _now():
    """The Module Reports A Formatted Time."""
    ymd = (strftime('%Y%m%d_%H%M%S'))
    return ymd


class CoreSetup(object):
    """CoreSetup."""

    def __init__(self, x_coordinate=1, y_coordinate=1):
        """Module CoreSetup __init__."""
        super().__init__()
        self.adjustments = int(0)
        self.buy_all_button = (0, 0)
        self.buy_all_button_mercs = (0, 0)
        self.size = str(size())
        self.x_coordinate = int(10)
        self.y_coordinate = int(10)

    def main(self, x_coordinate=1, y_coordinate=1):
        """SET WindowSize Based On Screen Dimensions."""
        if str(size()) == 'Size(width=1440, height=900)':
            self.adjustments = int(0)
            self.buy_all_button = (298, 106)
            self.buy_all_button_mercs = (160, 106)
            self.size = (1440, 900)
            self.x_coordinate = int(600)
            self.y_coordinate = int(580)
            self.clickspeed = 0.0315
            return

        elif str(size()) == 'Size(width=1920, height=1080)':
            self.adjustments = int(60)
            self.buy_all_button = (900, 140)
            self.buy_all_button_mercs = (160, 106)
            self.size = (1920, 1080)
            self.x_coordinate = int(620)
            self.y_coordinate = int(620)
            self.clickspeed = 0.0315
            return

        else:
            print('No Setting for screen size: {}'.format(size()))
            print('No Setting for screen size: {}'.format(self.size))

            exit()


class NewGame(object):
    """Class for NewGame."""

    def __init__(self):
        """Module for NewGame initialization."""
        super().__init__()
        self.clicks = 0
        self.abdication = False
        self.abdication_confirmation = (420, 530)
        self.abdication_coordinates = (215, 75)
        self.proofofgooddeed = (190, 120)
        self.proofofevildeed = (215, 180)
        self.proofofneutrality = (215, 240)

    def abdicate(self, clicks=0):
        """The Module Has Been Built to start over."""
        print("{} Abdication.".format(_now()))
        click(self.abdication_coordinates[0],
              self.abdication_coordinates[1],
              self.clicks)
        click(self.abdication_confirmation[0],
              self.abdication_confirmation[1],
              self.clicks)

    def proofofgooddeed(self, clicks=0):
        """The Module Has Been Built to start over."""
        print("{} Proof Of Good Deed.".format(_now()))
        click(self.proofofgooddeed[0], self.proofofgooddeed[1], self.clicks)

    def proofofevildeed(self, clicks=0):
        """The Module Has Been Built to start over."""
        print("{} Proof Of Evil Deed.".format(_now()))
        click(self.proofofevildeed[0], self.proofofevildeed[1], self.clicks)

    def proofofneutrality(self, clicks=0):
        """The Module Has Been Built to start over."""
        print("{} Proof Of Neutrality.".format(_now()))
        click(self.proofofneutrality[0], self.proofofneutrality[1],
              self.clicks)

    def main(self):
        """Module NewGame main."""
        NewGame.abdicate(self, clicks=0)
        NewGame.proofofgooddeed(self, clicks=0)
        NewGame.proofofevildeed(self, clicks=0)
        NewGame.proofofneutrality(self, clicks=0)


class Clickin(object):
    """Class for NewGame."""

    # set outside for random reference by modules
    random_choice_mouse_move = [easeInQuad,
                                easeOutQuad,
                                easeInOutQuad,
                                easeInBounce,
                                easeInElastic
                                ]

    def __init__(self, x_coordinate=0, y_coordinate=0):
        """Module to move mouse to xy coordinate."""
        super().__init__()
        self.x_coordinate = CoreSetup.x_coordinate
        self.y_coordinate = CoreSetup.y_coordinate
        self.clickspeed = 0.0315

    def strightclickin(self, x_coordinate=0, y_coordinate=0, numberofclicks=1,
                       clickspeed=0.0315):
        """Docs."""
        current_display_info = CoreSetup()
        CoreSetup.main(current_display_info)
        x_coordinate = int((current_display_info.x_coordinate))
        y_coordinate = int((current_display_info.y_coordinate))

        moveTo(x_coordinate, y_coordinate,
               # create a random float between 0.01 and 1.00
               # intended to be more....human like..sorta.
               float("{:00.2f}".format(round(uniform(1, 100) * .01, 2))),
               # choose a random mouse movement type from pyautogui
               # intended to be more....human like..sorta.
               choice(Clickin.random_choice_mouse_move))
        click(x_coordinate, y_coordinate,
              clicks=numberofclicks,
              interval=clickspeed,
              button='left'
              )

    def main(self):
        """Module NewGame main."""
        Clickin.strightclickin(160, 106, 1)
        Clickin.strightclickin(numberofclicks=1)


if __name__ == "__main__":

    if (os.name == 'posix' and
            platform.system() == 'Darwin' and
            platform.python_version() == '3.7.2'):
        pass
        Clickin.strightclickin(160, 106, 1)
    else:
        exit('Supported by Python 3.7.0 and on OSX only at this time.')
        print("{}".format(os.name))

    # print("{} has been called from {}".format(__file__, __name__))
    current_display_info = CoreSetup()
    pprint(vars(current_display_info))

    # current_display_info = NewGame()
    pprint(vars(current_display_info))

    # current_display_info = Clickin()
    pprint(vars(current_display_info))
