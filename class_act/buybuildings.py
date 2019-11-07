#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module buybuildings is Built for the Steam Game 'Realm Grinder'.

Buy all available Buildings.
"""
# =============================================================================
from random import shuffle
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


def human_variance():
    """The Module change the speed for each round of clicks you do.

    Returns: Float(Number) between 1.00 <=> 0.00
    """
    z = float("{:00.2f}".format(round(uniform(0, 100) * .01, 2)))
    return z


def buybuildings(clicks):
    """Module To Buy All Buildings (Farm to Hall of Legends)."""
    total_clicks = 0
    clicks += 0
    for i in Y_CORDINATE:
        click(X_CORDINATE[0], i + ADJUSTMENTS, clicks, CLICK_SPEED)
    total_clicks = clicks * len(Y_CORDINATE)
    return total_clicks


def buyrandombuildingslist(clicks):
    """Module To Buy All Buildings In Random Order."""
    total_clicks = 0
    clicks += 0
    x = list(Y_CORDINATE)
    shuffle(x)
    for i in x:
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
    print("{} when called directly"
          " does NOT click but shows location".format(__file__))
    buyrandombuildingslist(0)
    buybuildings(0)
    buybuildingsrev(0)
