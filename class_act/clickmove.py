#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'.

And is defining either `strightclickin` for Neutral or Evil Alignment.
And is defining either `clickmove` for Good Alignment,
To get the most from Dwarven upgrades.
"""
import random

from detectwindowsize import DetectWindowSize

from pyautogui import click


def strightclickin(count_me=50):
    """Docs."""
    dws = DetectWindowSize()
    DetectWindowSize.main(dws)
    x_cordinate = int((dws.x_cordinate))
    y_cordinate = int((dws.y_cordinate))
    click(int((x_cordinate)) + 0,
          int((y_cordinate)) + 0,
          clicks=count_me,
          interval=0.037,
          button='left'
          )


def clickmove(count_me=50):
    """"The clickmove is a Module is for Good Players using Dwarven.

    This func is required to keep making the most money while clicking.
    you must move every 25-50 clicks otherwise you loose the %600 bonus.
    """
    dws = DetectWindowSize()
    DetectWindowSize.main(dws)
    x_cordinate = int((dws.x_cordinate))
    y_cordinate = int((dws.y_cordinate))
    count = 1
    count_upto_me = count_me
    _start_number = 0
    _interval = 25
    total_clicks_left = int(count_upto_me)

    for count in range(_start_number, count_upto_me, _interval):
        click(int((x_cordinate)) + (random.randint(-25, 25)),
              int((y_cordinate)) + (random.randint(-25, 25)),
              clicks=_interval,
              interval=0.037,
              button='left'
              )

        count += _interval
        total_clicks_left -= _interval


if __name__ == "__main__":
    print("{} has been called from {}".format(__file__, __name__))
    strightclickin(count_me=10)
    clickmove(count_me=250)
