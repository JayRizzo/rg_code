#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'."""
# =============================================================================
# Laptop Screen Size Directly Correlates to the x, y axis of mouse navigation.
# Note: Currently SPECIFICALLY ONLY WORKS WITH VERSION "PyAutoGUI 0.9.44 !!!"
# TO INSTALL USE:    pip3 install 'pyautogui==0.9.44' --force --upgrade
# =============================================================================
from os import name as osname
import platform

from sys import argv

from factions import angels
from factions import clickinupgrades
from factions import demon
from factions import druid
from factions import elven
from factions import faceless
from factions import fairy
from factions import goblin
from factions import mercenary
from factions import titan
from factions import undead

# https://stackoverflow.com/a/48728321/1896134
dont_write_bytecode = True


if __name__ == "__main__":
    if osname == "posix" and platform.system() == "Darwin":
        if len(argv) == 1:
            exit("Must Specify A Faction to buy buildings, upgrades & make $$$"
                 "\n====== Good ======\n"
                 "Fairy, Elven, Angel\n"
                 "\n====== Evil ======\n"
                 "Goblin, Undead, Demon\n"
                 "\n====== Neutral ======\n"
                 "Titan, Druid, Faceless\n"
                 "\n====== Others ======\n"
                 "Mercenary (mercs or merc)\n"
                 "\n====== Make Money ======\n"
                 "clickinupgrades\n")

        if len(argv) == 2:
            # Good Factions
            if argv[1].__str__().lower().strip() == "fairy":
                fairy()
            elif argv[1].__str__().lower().strip() == "elven":
                elven()
            elif argv[1].__str__().lower().strip() == "angel":
                angels()
            # Evil Factions
            elif argv[1].__str__().lower().strip() == "goblin":
                goblin()
            elif argv[1].__str__().lower().strip() == "undead":
                undead()
            elif argv[1].__str__().lower().strip() == "demon":
                demon()
            # Neutral Factions
            elif argv[1].__str__().lower().strip() == "titan":
                titan()
            elif argv[1].__str__().lower().strip() == "druid":
                druid()
            elif argv[1].__str__().lower().strip() == "faceless":
                faceless()
            elif argv[1].__str__().lower().strip() == "mercenary":
                mercenary()
            elif argv[1].__str__().lower().strip() == "mercs":
                mercenary()
            elif argv[1].__str__().lower().strip() == "merc":
                mercenary()
            elif argv[1].__str__().lower().strip() == "clickinupgrades":
                clickinupgrades()
            else:
                exit("Unknown Faction: {}.".format(argv[1].__str__()))
        elif len(argv) > 2:
            exit('Unknown Extra Arguments: {}'.format(argv[2:].__str__()))
    else:
        print("{}".format(platform.system()))
        exit("Supported by OSX only at this time.")
