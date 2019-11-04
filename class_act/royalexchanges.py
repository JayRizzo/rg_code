#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'."""
# =============================================================================

import time

from pyautogui import click


class BuyAllRoyalExchanges(object):
    """Class BuyAllRoyalExchanges."""

    def __init__(self, arg):
        """Example."""
        super(BuyAllRoyalExchanges, self).__init__()
        self.arg = arg

    def buyallexchange():
        """The buyallexchange is to buy all available upgrades."""
        print("%s Buying all Royal Exchanges." % (time.ctime()))
        # openroyalexchangebutton()
        # fairyexchange()
        # elvenexchange()
        # angelexchange()
        # goblinexchange()
        # undeadexchange()
        # demonexchange()
        # dwarvenexchange()
        # drowexchange()
        # closeroyalexchangebutton()

    def openroyalexchangebutton():
        """The openroyalexchangebutton is to open pop-up."""
        click(120, 190, clicks=1, interval=0.0325, button="left")

    def closeroyalexchangebutton():
        """The closeroyalexchangebutton is to close pop-up."""
        click(800, 200, clicks=1, interval=0.0325, button="left")

    def fairyexchange():
        """The Fairy exchange is to buy one or more available upgrades."""
        click(710, 270, clicks=1, interval=0.0325, button="left")

    def elvenexchange():
        """The Elven exchange is to buy one or more available upgrades."""
        click(710, 320, clicks=1, interval=0.0325, button="left")

    def angelexchange():
        """The Angel exchange is to buy one or more available upgrades."""
        click(710, 370, clicks=1, interval=0.0325, button="left")

    def goblinexchange():
        """The Goblin exchange is to buy one or more available upgrades."""
        click(710, 420, clicks=1, interval=0.0325, button="left")

    def undeadexchange():
        """The Undead exchange is to buy one or more available upgrades."""
        click(710, 470, clicks=1, interval=0.0325, button="left")

    def demonexchange():
        """The Demon exchange is to buy one or more available upgrades."""
        click(710, 520, clicks=1, interval=0.00325, button="left")

    def dwarvenexchange():
        """The Dwarven exchange is to buy one or more available upgrades."""
        click(710, 570, clicks=1, interval=0.0325, button="left")

    def drowexchange():
        """The Drow exchange is to buy one or more available upgrades."""
        click(710, 620, clicks=1, interval=0.0325, button="left")
