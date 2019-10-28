#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module buyallupgradesbutton is Built for the Steam Game 'Realm Grinder'.

Buy all available upgrades.
"""
# =============================================================================
from pyautogui import click
CLICK_SPEED = 0.0037
# CLICK_SPEED = 0.0315


def buyallupgradesbutton(clicks):
    """The buyallupgradesbutton is to buy all available upgrades."""
    click(298, 106, clicks=clicks, interval=CLICK_SPEED, button="left")
    return clicks


def buyallupgradesbuttonmercenary(clicks):
    """The buyallupgradesbuttonmercenary is to buy all available upgrades."""
    click(160, 106, clicks=clicks, interval=0.0037, button="left")
    return clicks


if __name__ == "__main__":
    print("{} has been called from {}".format(__file__, __name__))
    buyallupgradesbutton(0)
    buyallupgradesbuttonmercenary(0)
