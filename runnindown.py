#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module Has Been Built for the Steam Game 'Realm Grinder'."""
# Laptop Screen Size Directly Correlates to the x, y axis of mouse navigation.
# Note: Currently SPECIFICALLY ONLY WORKS WITH VERSION "PyAutoGUI 0.9.44 !!!"
# TO INSTALL USE:    pip3 install 'pyautogui==0.9.44' --force --upgrade
# =============================================================================
from datetime import datetime
from random import choice
from time import sleep
from time import strftime

from pyautogui import click

# =============================================================================
# GLOBALS
# =============================================================================
# Y_AXIS \/
BUILDING_TO_BUY = [200, 260, 320, 380, 440, 500, 560, 620, 680, 740, 800, ]
X_AXIS = 920  # USED TO LOCATE THE BUYING HORIZONTAL LOC.

CLICK_SPEED = 0.0315  # REALM GRINDER DESKTOP CAN'T REGISTAR QUICKER THAN THIS.

# =============================================================================
# FUNCTIONS
# =============================================================================


def _now():
    """The Module Returns "Current Time" As A Formatted String."""
    ymd = str(strftime('%Y%m%d_%H%M%S'))
    return ymd


def buyingupgrades(clicks):
    """The Module buyallbutton upgrades and exchanges."""
    upgradeclicks = clicks + 0
    click(298, 106, clicks, CLICK_SPEED)
    return upgradeclicks


def buyingupgrades_mercs(clicks):
    """The Module buyallbutton upgrades and exchanges."""
    upgradeclicks = clicks + 0
    click(160, 106, clicks, CLICK_SPEED)
    return upgradeclicks


def buyingbuildingsrandom(clicks):
    """The Module buy all buildings at random."""
    randombuildingclicks = clicks + 0
    selectedz = choice(BUILDING_TO_BUY)
    click(X_AXIS, selectedz + 10, clicks, CLICK_SPEED)  # 01
    return randombuildingclicks


def buyingbuildings(clicks):
    """Module To Buy All Buildings."""
    clicks = clicks + 0
    for _ in range(11):
        click(X_AXIS, BUILDING_TO_BUY[_] + 20, clicks, CLICK_SPEED)  # 01
    total_clicks = clicks * 11
    return total_clicks


def buyingbuildingsrev(clicks):
    """The Module buy all buildings but Reversed."""
    clicks = clicks + 0
    building_to_buy = BUILDING_TO_BUY[::-1]
    for _ in range(len(BUILDING_TO_BUY)):
        click(X_AXIS, int(building_to_buy[_]) + 20, clicks, CLICK_SPEED)  # 01
    total_clicks = clicks * 11
    return total_clicks


def angelbuyingbuildings(clicks):
    """The Module buy all Starting With "Heavens Domain" buildings."""
    clicks = clicks + 0
    click(X_AXIS, 620, clicks, CLICK_SPEED)  # 08
    click(X_AXIS, 740, clicks, CLICK_SPEED)  # 10
    click(X_AXIS, 320, clicks, CLICK_SPEED)  # 03
    click(X_AXIS, 800, clicks, CLICK_SPEED)  # 11
    click(X_AXIS, 680, clicks, CLICK_SPEED)  # 09
    click(X_AXIS, 200, clicks, CLICK_SPEED)  # 01
    click(X_AXIS, 260, clicks, CLICK_SPEED)  # 02
    click(X_AXIS, 320, clicks, CLICK_SPEED)  # 03
    click(X_AXIS, 380, clicks, CLICK_SPEED)  # 04
    click(X_AXIS, 440, clicks, CLICK_SPEED)  # 05
    click(X_AXIS, 500, clicks, CLICK_SPEED)  # 06
    click(X_AXIS, 560, clicks, CLICK_SPEED)  # 07
    click(X_AXIS, 620, clicks, CLICK_SPEED)  # 08
    click(X_AXIS, 680, clicks, CLICK_SPEED)  # 09
    click(X_AXIS, 740, clicks, CLICK_SPEED)  # 10
    click(X_AXIS, 800, clicks, CLICK_SPEED)  # 11
    total_clicks = clicks * 11
    return total_clicks


def _abdicate(clicks):
    """The Starts a New Game."""
    clicks = clicks + 0
    click(215, 75, clicks, CLICK_SPEED)
    sleep(0.03)
    click(420, 530, clicks, CLICK_SPEED)
    sleep(0.03)
    return clicks


def _good_alignment(clicks):
    """The Selects A good Alignment."""
    clicks = clicks + 0
    click(190, 120, clicks, CLICK_SPEED)
    return clicks


def _evil_alignment(clicks):
    """The Selects A Evil Alignment."""
    clicks = clicks + 0
    click(215, 180, clicks, CLICK_SPEED)
    return clicks


def _neutral_alignment(clicks):
    """The Selects A Neutral Alignment."""
    clicks = clicks + 0
    click(215, 240, clicks, CLICK_SPEED)
    return clicks


def new_good_game(clicks):
    """The Starts a New Game Good alignment."""
    clicks = clicks + 0
    _abdicate(clicks)
    _good_alignment(clicks)
    buyingupgrades(clicks)
    makemoney(100)
    buyingbuildingsrev(clicks)
    buyingbuildings(clicks)
    buyingupgrades(clicks)
    return clicks


def new_evil_game(clicks):
    """The Starts a New Game Evil alignment."""
    clicks = clicks + 0
    _abdicate(clicks)
    _evil_alignment(clicks)
    buyingupgrades(clicks)
    makemoney(100)
    buyingbuildingsrev(clicks)
    buyingbuildings(clicks)
    buyingupgrades(clicks)
    return clicks


def new_neutral_game(clicks):
    """The Starts a New Game Neutral alignment."""
    clicks = clicks + 0
    _abdicate(clicks)
    _neutral_alignment(clicks)
    buyingupgrades(clicks)
    makemoney(100)
    buyingbuildingsrev(clicks)
    buyingbuildings(clicks)
    buyingupgrades(clicks)
    return


def makemoney(clicks):
    """The Module Clicks For Money Time."""
    makemoneyclicks = clicks + 0
    click(560, 438, clicks, CLICK_SPEED)
    return makemoneyclicks


def makemoney2(clicks):
    u"""The Module Clicks For $£¢ !  Moves for Dwarven Requirement < R45?."""
    clicks = clicks + 0
    click(570, 438, clicks, CLICK_SPEED)
    click(663, 438, clicks, CLICK_SPEED)
    return clicks * 2


def basic_run(moneyclicks, clicksbuilding, upgrades, mercz):
    """The Speeds Up New Game Gem Grinding."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    total_clicks_purchased = 0
    last_total_time_elapsed = 0
    total_time_elapsed = 0
    upgrades = upgrades + 0
    moneyclicks = moneyclicks + 0
    clicksbuilding = clicksbuilding + 0
    for _ in range(9999999999):
        _start = datetime.now()
        total_upgrades_purchased += upgrades * 2
        total_buildings_purchased += (clicksbuilding * 22) + (22 * 4)
        total_clicks_purchased += moneyclicks
        if mercz:
            buyingupgrades_mercs(upgrades)
        else:
            buyingupgrades(upgrades)
        buyingbuildingsrandom(clicksbuilding)
        buyingbuildingsrandom(clicksbuilding)
        buyingbuildingsrev(clicksbuilding)
        buyingbuildingsrandom(clicksbuilding)
        buyingbuildingsrandom(clicksbuilding)
        makemoney(moneyclicks)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        print("{} Round {} TT: {} T: {} TD: {} B: {} U: {} C: {} TC: {}."
              "".format(_now(),
                        "{:04.0f}".format(_ + 1),
                        "{:07.3f}".format(total_time_elapsed),
                        "{:07.3f}".format((_end - _start).total_seconds()),
                        "{:07.3f}".format((_end - _start).total_seconds() -
                                          last_total_time_elapsed),
                        "{:04.0f}".format(total_buildings_purchased),
                        "{:04.0f}".format(total_upgrades_purchased),
                        "{:04.0f}".format(moneyclicks),
                        "{:04.0f}".format(total_clicks_purchased)
                        )
              )
        last_total_time_elapsed = (_end - _start).total_seconds()
        moneyclicks += 25


if __name__ == "__main__":
    basic_run(25, 5, 1, False)
