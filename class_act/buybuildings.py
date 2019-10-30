#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module buybuildings is Built for the Steam Game 'Realm Grinder'.

Buy all available Buildings.
"""
# =============================================================================
from random import choice
from random import uniform

from detectwindowsize import DetectWindowSize

from pyautogui import click
from pyautogui import easeInBounce
from pyautogui import easeInElastic
from pyautogui import easeInOutQuad
from pyautogui import easeInQuad
from pyautogui import easeOutQuad
# from pyautogui import moveTo

detectws = DetectWindowSize()
DetectWindowSize.main(detectws)
ADJUSTMENTS = detectws.adjustments
X_CORDINATE = [900, ]
Y_CORDINATE = [140, 200, 260, 320, 380, 440, 500, 560, 620, 680, 740, ]
CLICK_SPEED = 0.001  # RG Lags a bit but works this fast for buildings
RANDOM_MOUSE = [easeInQuad,
                easeOutQuad,
                easeInOutQuad,
                easeInBounce,
                easeInElastic
                ]


# # @CallCount
# def buy_allbauildings(buy_clicks=1):
#     """Docs."""
#     # print("%s Buying all available buildings." % (time.ctime()))
#     Y_CORDINATE[0],
#     Y_CORDINATE[1],
#     Y_CORDINATE[2],
#     Y_CORDINATE[3],
#     Y_CORDINATE[4],
#     Y_CORDINATE[5],
#     Y_CORDINATE[6],
#     Y_CORDINATE[7],
#     Y_CORDINATE[8],
#     Y_CORDINATE[9],
#     Y_CORDINATE[10],
#     return


def human_variance():
    """The Module change the speed for each round of clicks you do.

    Returns: Float(Number) between 1.00 <=> 0.00
    """
    z = float("{:00.2f}".format(round(uniform(0, 100) * .01, 2)))
    return z


def buyrandombuildings(clicks):
    """The Module buy all buildings at random."""
    clicks += 0
    selectedz = choice(Y_CORDINATE) + ADJUSTMENTS
    # moveTo(x=X_CORDINATE[0],
    #        y=selectedz,
    #        duration=round(uniform(25, 100) * .01, 2),
    #        tween=choice(RANDOM_MOUSE)
    #        )
    click(x=X_CORDINATE[0],
          y=selectedz,
          clicks=clicks,
          interval=CLICK_SPEED
          # interval=human_variance()
          )
    return clicks


def buybuildings(clicks):
    """Module To Buy All Buildings (Farm to Hall of Legends)."""
    total_clicks = 0
    clicks += 0
    for i in Y_CORDINATE:
        click(X_CORDINATE[0], i + ADJUSTMENTS, clicks, CLICK_SPEED)
    total_clicks = clicks * len(Y_CORDINATE)
    return total_clicks


def buybuildingsrev(clicks):
    """The Module buy all buildings but Reversed (Hall of Legends to Farms)."""
    total_clicks = 0
    clicks += 0
    # for i in Y_CORDINATE[::-1]:  # same as below
    for i in reversed(Y_CORDINATE):
        click(X_CORDINATE[0], i + ADJUSTMENTS, clicks, CLICK_SPEED)
    total_clicks = clicks * len(Y_CORDINATE)
    return total_clicks


if __name__ == "__main__":
    print("{} has been called from {}".format(__file__, __name__))
    buyrandombuildings(0)
    buybuildings(0)
    buybuildingsrev(0)


# help(click)
# click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0,
#       tween=<function linear at 0x10fff20e0>, pause=None, _pause=True)
# help(moveTo)
# moveTo(x=None, y=None, duration=0.0, tween=<function linear at 0x10fff20e0>,
#        pause=None, _pause=True)
