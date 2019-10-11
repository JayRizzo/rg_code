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

from buybuildings import buy_allbuildings as bab
from buybuildings import buy_allbuildings_rev as babre
from buybuildings import buyrandombuildings as brb

from clickmove import clickmove
from clickmove import strightclickin

SLEEPTIME = 10


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


def fairies():
    """The Module Has Been Built for the Fairy Race."""
    clicks = 2500
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        brb(1)
        bab(1)
        babre(1)
        for _pony in range(10):
            brb(1)
        clickmove(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def elven():
    """The Module Has Been Built for the Elven Race."""
    clicks = 2500
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        brb(1)
        brb(1)
        babre(1)
        for _pony in range(10):
            brb(1)
        clickmove(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def angels(clicks=None):
    """The Module Has Been Built for the Angels Race."""
    clicks = 2500
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
    clicks = 2500
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
    clicks = 2500
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
    clicks = 2500
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(1)
        for _pony in range(10):
            brb(1)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def titan(clicks=None):
    """The Module Has Been Built for the Titan Race."""
    clicks = 2500
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(1)
        for _pony in range(10):
            brb(1)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def druid(clicks=None):
    """The Module Has Been Built for the Druid Race."""
    clicks = 2500
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(1)
        for _pony in range(10):
            brb(1)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def faceless(clicks=None):
    """The Module Has Been Built for the Faceless Race."""
    clicks = 2500
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    for _ in range(99999999999999999):
        start = datetime.now()
        bau(1)
        babre(1)
        for _pony in range(10):
            brb(1)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def mercenary(clicks=None):
    """The Module Has Been Built for the Mercenary Race."""
    clicks = 2500
    for _ in range(99999999999999999):
        start = datetime.now()
        baum(1)
        babre(1)
        for _pony in range(10):
            brb(1)
        strightclickin(clicks)
        end = datetime.now()
        timerz(_, start, end, clicks)


def clickinupgrades():
    """The Module Has Been Built for All Races.

    The Design is for upgrades and clickin only.
    """
    clicks = 2500
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
