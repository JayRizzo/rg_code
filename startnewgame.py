#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'."""
# =============================================================================
import time

import pyautogui


def abdicate():
    """The Module Has Been Built to start over."""
    print("%s Abdication." % (time.ctime()))
    pyautogui.click(215, 75, clicks=1, interval=0.1, button='left')
    pyautogui.click(420, 530, clicks=1, interval=0.1, button='left')


def proofofgooddeed():
    """The Module Has Been Built to start over."""
    print("%s Proof Of Good Deed." % (time.ctime()))
    pyautogui.click(190, 120, clicks=1, interval=0.1, button='left')


def proofofevildeed():
    """The Module Has Been Built to start over."""
    print("%s Proof Of Evil Deed." % (time.ctime()))
    pyautogui.click(215, 180, clicks=1, interval=0.1, button='left')


def proofofneutrality():
    """The Module Has Been Built to start over."""
    print("%s Proof Of Neutrality." % (time.ctime()))
    pyautogui.click(215, 240, clicks=1, interval=0.1, button='left')
