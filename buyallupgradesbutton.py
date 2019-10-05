#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'."""
# =============================================================================
from pyautogui import click
CLICK_SPEED = 0.0037
# CLICK_SPEED = 0.0315


def buyallupgradesbutton(clicks):
    """The buyallupgradesbutton is to buy all available upgrades."""
    click(298, 106, clicks=clicks, interval=CLICK_SPEED, button="left")


def buyallupgradesbuttonmercenary(clicks):
    """The buyallupgradesbuttonmercenary is to buy all available upgrades."""
    click(160, 106, clicks=clicks, interval=0.0037, button="left")
