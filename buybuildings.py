#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module Has Been Built for the Steam Game 'Realm Grinder'."""
# =============================================================================
import random

from detectwindowsize import DetectWindowSize

import pyautogui

DETECTWS = DetectWindowSize()
DetectWindowSize.main(DETECTWS)
X_CORDINATE = 900
Y_CORDINATE = 140
ADJUSTMENTS = int((DETECTWS.adjustments))
BUTTON_SPEED = 0.005
# BUTTON_SPEED = 0.0315


def buyrandombuildings(buy_clicks=0):
    """Docs."""
    randombuildings = [
        buy_first,
        buy_second,
        buy_third,
        buy_fourth,
        buy_fifth,
        buy_sixth,
        buy_seventh,
        buy_eighth,
        buy_nineth,
        buy_tenth,
        buy_eleventh,
    ]
    return random.choice(randombuildings)(buy_clicks)


def buy_allbuildings(buy_clicks=0):
    """PlaceHolder."""
    # print("%s Buying all available buildings." % (time.ctime()))
    buy_first(buy_clicks)
    buy_second(buy_clicks)
    buy_third(buy_clicks)
    buy_fourth(buy_clicks)
    buy_fifth(buy_clicks)
    buy_sixth(buy_clicks)
    buy_seventh(buy_clicks)
    buy_eighth(buy_clicks)
    buy_nineth(buy_clicks)
    buy_tenth(buy_clicks)
    buy_eleventh(buy_clicks)


def buy_allbuildings_rev(buy_clicks=0):
    """PlaceHolder."""
    # print("%s Buying all available buildings reverse." % (time.ctime()))
    buy_eleventh(buy_clicks)
    buy_tenth(buy_clicks)
    buy_nineth(buy_clicks)
    buy_eighth(buy_clicks)
    buy_seventh(buy_clicks)
    buy_sixth(buy_clicks)
    buy_fifth(buy_clicks)
    buy_fourth(buy_clicks)
    buy_third(buy_clicks)
    buy_second(buy_clicks)
    buy_first(buy_clicks)


def buy_first(buy_clicks=0):
    """The Module Has Been Built to buy # FARMS (1)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 0 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_second(buy_clicks=0):
    """The Module Has Been Built to buy # INNS (2)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 60 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_third(buy_clicks=0):
    """The Module Has Been Built to buy # BLACK SMITH (3)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 120 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_fourth(buy_clicks=0):
    """The Module Has Been Built to buy # SLAVE PEN (4)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 180 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_fifth(buy_clicks=0):
    """The Module Has Been Built to buy # ORCISH ARENA (5)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 240 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_sixth(buy_clicks=0):
    """The Module Has Been Built to buy # WITCH CONCLAVE (6)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 300 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_seventh(buy_clicks=0):
    """The Module Has Been Built to buy # DARK TEMPLE (7)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 360 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_eighth(buy_clicks=0):
    """The Module Has Been Built to buy # NECROPOLIS (8)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 420 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_nineth(buy_clicks=0):
    """The Module Has Been Built to buy # EVIL FORTRESS (9)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 480 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_tenth(buy_clicks=0):
    """The Module Has Been Built to buy # HELL PORTAL (10)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 540 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )


def buy_eleventh(buy_clicks=0):
    """The Module Has Been Built to buy # HALL OF LEGENDS (11)."""
    pyautogui.click(X_CORDINATE,
                    Y_CORDINATE + 600 + ADJUSTMENTS,
                    clicks=buy_clicks,
                    interval=BUTTON_SPEED,
                    button='left'
                    )
