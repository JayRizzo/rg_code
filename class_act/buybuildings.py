#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module buybuildings is Built for the Steam Game 'Realm Grinder'.

Buy all available Buildings.
"""
# =============================================================================
from random import choice

from detectwindowsize import DetectWindowSize

from pyautogui import click

detectws = DetectWindowSize()
DetectWindowSize.main(detectws)

ADJUSTMENTS = detectws.adjustments
X_CORDINATE = [900, ]
Y_CORDINATE = [140, 200, 260, 320, 380, 440, 500, 560, 620, 680, 740, ]
CLICK_SPEED = 0.001  # RG Lags a bit but works this fast for buildings


def buyrandombuildings(clicks):
    """The Module buy all buildings at random."""
    clicks += 0
    selectedz = choice(Y_CORDINATE)
    click(X_CORDINATE[0], selectedz + ADJUSTMENTS, clicks, CLICK_SPEED)
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
