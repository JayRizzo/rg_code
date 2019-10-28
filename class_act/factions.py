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
CLICK_SPEED = 0.037  # REALM GRINDER DESKTOP CANNOT REGISTAR QUICKER THAN THIS!
MONEYCLICKS = 25
UPGRADES = 1
BUILDINGS = 10  # Module buys 10 in less than 1 sec each


def _now():
    """The Module Reports A Formatted Time."""
    ymd = (strftime("%Y%m%d_%H%M%S"))
    return ymd


def timerz(roundnum, _start, _end,
           moneyclicks=0, total_clicks=0,
           clicksbuilding=0, total_buildings_purchased=0,
           upgrades=0, total_upgrades_purchased=0,
           total_time_elapsed=0, last_total_time_elapsed=0):
    """The Module Reports A Formatted Timer."""
    print("{} Round {} TT: {} T: {} TD: {} TB: {} B: {} U: {} C: {} TC: {}."
          "".format(_now(),
                    "{:04.0f}".format(roundnum + 1),
                    "{:07.3f}".format(total_time_elapsed),
                    "{:07.3f}".format((_end - _start).total_seconds()),
                    "{:07.3f}".format((_end - _start).total_seconds() -
                                      last_total_time_elapsed),
                    "{:04.0f}".format(total_buildings_purchased),
                    "{:04.0f}".format(clicksbuilding),
                    "{:04.0f}".format(total_upgrades_purchased),
                    "{:04.0f}".format(moneyclicks),
                    "{:04.0f}".format(total_clicks)
                    )
          )
    last_total_time_elapsed = (_end - _start).total_seconds()


def fairies(clicks=None):
    """The Module Has Been Built for the Fairy Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += bab(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += clickmove(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 25


def elven(clicks=None):
    """The Module Has Been Built for the Elven Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += clickmove(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 25


def angels(clicks=None):
    """The Module Has Been Built for the Angels Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += clickmove(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 25


def goblin(clicks=None):
    """The Module Has Been Built for the Goblin Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 25


def undead(clicks=None):
    """The Module Has Been Built for the Undead Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 25


def demon(clicks=None):
    """The Module Has Been Built for the Demon Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 25


def titan(clicks=None):
    """The Module Has Been Built for the Titan Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 25


def druid(clicks=None):
    """The Module Has Been Built for the Druid Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 50


def faceless(clicks=None):
    """The Module Has Been Built for the Faceless Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += bau(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += bau(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 250


def mercenary(clicks=None):
    """The Module Has Been Built for the Mercenary Race."""
    total_upgrades_purchased = 0
    total_buildings_purchased = 0
    clicks = MONEYCLICKS + 0
    last_total_time_elapsed = 0
    total_clicks = 0
    total_time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        total_upgrades_purchased += baum(UPGRADES)
        total_buildings_purchased += babre(BUILDINGS)
        for _pony in range(10):
            total_buildings_purchased += brb(BUILDINGS)
        total_upgrades_purchased += baum(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        total_time_elapsed += (_end - _start).total_seconds()
        timerz(_, _start, _end,
               moneyclicks=clicks,
               total_clicks=total_clicks,
               clicksbuilding=BUILDINGS,
               total_buildings_purchased=total_buildings_purchased,
               upgrades=UPGRADES,
               total_upgrades_purchased=total_upgrades_purchased,
               total_time_elapsed=total_time_elapsed,
               last_total_time_elapsed=last_total_time_elapsed
               )
        last_total_time_elapsed = (_end - _start).total_seconds()
        clicks += 250


def clickinupgrades(clicks=None, merx=False):
    """The Module Has Been Built for All races.

    The Design is for upgrades and clickin only.
    """
    clicks = MONEYCLICKS  # pass constant into variable.
    print("{}: Starting Clicks Per Round {}.".format(_now(), clicks))
    total_clicks = 0
    total_time_elapsed = 0
    time_elapsed = 0
    for _ in range(99999999999999999):
        _start = datetime.now()
        if merx:
            baum(UPGRADES)
        else:
            bau(UPGRADES)
        total_clicks += strightclickin(clicks, CLICK_SPEED)
        _end = datetime.now()
        time_elapsed = (_end - _start).total_seconds()
        total_time_elapsed += (total_time_elapsed + time_elapsed)
        print("{_time}:"
              " Round: {_round:05d}"
              " Clicks: {_clicks:05d}"
              " Total Clicks: {_tclicks:07d}."
              " TimeElapsed: {_seconds:07.3f} sec"
              " TTimeElapsed: {_tseconds:09.3f} sec"
              "".format(_time=(_now()),
                        _round=(_ + 1),
                        _clicks=clicks,
                        _tclicks=total_clicks,
                        _seconds=time_elapsed,
                        _tseconds=total_time_elapsed,
                        )
              )
        clicks += 25


if __name__ == "__main__":
    if os.name == "posix" and platform.system() == "Darwin":
        # print("{}".format(platform.system()))
        pass
    else:
        exit("Supported by OSX only at this time.")
        print("{}".format(platform.system()))
