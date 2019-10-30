#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'.

And is defining either `strightclickin` for Neutral or Evil Alignment.
And is defining either `clickmove` for Good Alignment,
To get the most from Dwarven upgrades.
"""

from random import randint
from random import uniform

from detectwindowsize import DetectWindowSize

from pyautogui import click
from pyautogui import easeInOutQuad
from pyautogui import moveTo

dws = DetectWindowSize()
DetectWindowSize.main(dws)
X_CORD = dws.x_cordinate
Y_CORD = dws.y_cordinate
ADJUST = dws.adjustments


def strightclickin(count_me, click_speed=0.037):
    """Docs."""
    count_me += 0
    moveTo(X_CORD, Y_CORD, round(uniform(1, 100) * .01, 2))
    click(X_CORD, Y_CORD, clicks=count_me, interval=click_speed, button='left')
    return count_me


def clickmove(count_me=50, click_speed=0.037):
    """"The clickmove is a Module is for Good Factions using Dwarven upgrade.

    This func is required to keep making the most money while clicking.
    you must move every 25-50 clicks otherwise you loose the %600 bonus.
    Required only for R2-R50?  Goes away after some point.
    """
    count = 1
    count_upto_me = count_me
    _start_number = 0
    _interval = 25
    total_clicks_left = int(count_upto_me)
    for count in range(_start_number, count_upto_me, _interval):
        click(X_CORD + (randint(-25, 25)) + ADJUST,
              Y_CORD + (randint(-25, 25)) + ADJUST,
              clicks=_interval,
              interval=click_speed,
              button='left',
              tween=easeInOutQuad
              )
        count += _interval
        total_clicks_left -= _interval
    return count_me


if __name__ == "__main__":
    print("{} has been called from {}".format(__file__, __name__))
    strightclickin(count_me=250)
    clickmove(count_me=250)
