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

ADJUSTMENTS = int(detectws.adjustments)
X_CORDINATE = [900, ]
Y_CORDINATE = [140, 200, 260, 320, 380, 440, 500, 560, 620, 680, 740, ]
CLICK_SPEED = 0.005


def buyrandombuildings(clicks=0):
    """The Module buy all buildings at random."""
    randombuildingclicks = clicks + 0
    selectedz = choice(Y_CORDINATE)
    click(X_CORDINATE[0], selectedz + ADJUSTMENTS, clicks, CLICK_SPEED)
    # print("buyrandombuildings: {}".format(clicks))
    return randombuildingclicks


def buybuildings(clicks):
    """Module To Buy All Buildings (Farm to Hall of Legends)."""
    total_clicks = 0
    clicks += 0
    for i in Y_CORDINATE:
        click(X_CORDINATE[0], i + ADJUSTMENTS, clicks, CLICK_SPEED)
    total_clicks = clicks * len(Y_CORDINATE)
    # print("buybuildings: {}".format(clicks))
    return total_clicks


def buybuildingsrev(clicks):
    """The Module buy all buildings but Reversed (Hall of Legends to Farms)."""
    total_clicks = 0
    clicks += 0
    # for i in Y_CORDINATE[::-1]:
    for i in reversed(Y_CORDINATE):
        click(X_CORDINATE[0], i + ADJUSTMENTS, clicks, CLICK_SPEED)
    total_clicks = clicks * len(Y_CORDINATE)
    # print("buybuildingsrev: {}".format(clicks))
    return total_clicks
