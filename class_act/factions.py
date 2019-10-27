#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'."""
# =============================================================================
import os
import platform
from datetime import datetime
from time import strftime

from buyallupgradesbutton import buyallupgradesbutton as bau
from buyallupgradesbutton import buyallupgradesbuttonmercenary as baum

from buybuildings import buybuildings as bab
from buybuildings import buybuildingsrev as babre
from buybuildings import buyrandombuildings as brb

from clickmove import clickmove
from clickmove import strightclickin

SLEEPTIME = 10
CLICK_SPEED = 0.0315  # REALM GRINDER DESKTOP CAN'T REGISTAR QUICKER THAN THIS.


def _now():
    """The Module Reports A Formatted Time."""
    ymd = (strftime('%Y%m%d_%H%M%S'))
    return ymd


def timerz(roundnum, start, end, clicks):
    """The Module Reports A Formatted Timer."""
    a = ("{}: TimeElapsed: {} Seconds, Clicks: {} x {} "
         "= {} clicks.".format(_now(),
                               "{:.5f}".format((end -
                                                start).total_seconds()),
                               clicks, roundnum + 1, ((roundnum + 1) * clicks),
                               )
         )
    print("{}".format(a))
    return a


def basic_run(moneyclicks,
              clicksbuilding,
              upgrades,
              mercz=False):
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
            baum(upgrades)
        else:
            bau(upgrades)
        brb(clicksbuilding)
        brb(clicksbuilding)
        babre(clicksbuilding)
        brb(clicksbuilding)
        brb(clicksbuilding)
        strightclickin(moneyclicks)
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
        moneyclicks += 250


def fairies():
    """The Module Has Been Built for the Fairy Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        brb(10)
        bab(10)
        babre(10)
        for _pony in range(10):
            brb(10)
        clickmove(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def elven():
    """The Module Has Been Built for the Elven Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        brb(10)
        brb(10)
        babre(10)
        for _pony in range(10):
            brb(10)
        clickmove(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def angels(clicks=None):
    """The Module Has Been Built for the Angels Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        for _pony in range(10):
            brb(10)
        clickmove(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def goblin(clicks=None):
    """The Module Has Been Built for the Goblin Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        for _pony in range(2):
            brb(10)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def undead(clicks=None):
    """The Module Has Been Built for the Undead Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(10)
        for _pony in range(2):
            brb(10)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def demon(clicks=None):
    """The Module Has Been Built for the Demon Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(10)
        for _pony in range(10):
            brb(10)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def titan(clicks=None):
    """The Module Has Been Built for the Titan Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(10)
        for _pony in range(10):
            brb(10)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def druid(clicks=None):
    """The Module Has Been Built for the Druid Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(10)
        for _pony in range(10):
            brb(10)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def faceless(clicks=None):
    """The Module Has Been Built for the Faceless Race."""
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(10)
        for _pony in range(5):
            brb(10)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)
        clicks += 25


def mercenary(clicks=None):
    """The Module Has Been Built for the Mercenary Race."""
    clicks = 250
    for _ in range(99999999999999999):
        start = datetime.now()
        baum(1)
        babre(10)
        for _pony in range(10):
            brb(10)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def clickinupgrades():
    """The Module Has Been Built for All Races.

    The Design is for upgrades and clickin only.
    """
    clicks = 250
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        clickmove(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


if __name__ == "__main__":
    if os.name == 'posix' and platform.system() == 'Darwin':
        # print("{}".format(platform.system()))
        pass
    else:
        exit('Supported by OSX only at this time.')
        print("{}".format(platform.system()))
