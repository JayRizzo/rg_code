#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'."""
# =============================================================================

import time

from pyautogui import click


def dwarvenchallenge2(x_cordinate=None, y_cordinate=None):
    """The dwarvenchallenge2 goal is to:.

    Pick Fairy Faction.
    Pick Dwarven Bloodline.
    Buy 2750 Inns Within 2 minutes of a new game.
    """
    if x_cordinate is None:
        x_cordinate = 360
    if y_cordinate is None:
        y_cordinate = 311
    print("%s Buying Initial Bloodline." % (time.ctime()))
    click(x_cordinate, y_cordinate,
          clicks=1,
          interval=0.0037,
          button="left"
          )

    x_cordinate = 427
    y_cordinate = 531

    click(x_cordinate, y_cordinate,
          clicks=1,
          interval=0.0037,
          button="left"
          )
