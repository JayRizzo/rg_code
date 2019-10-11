#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the Steam Game 'Realm Grinder'."""
# =============================================================================
from sys import argv

from factions import angels
from factions import clickinupgrades
from factions import demon
from factions import druid
from factions import elven
from factions import faceless
from factions import fairies
from factions import goblin
from factions import mercenary
from factions import titan
from factions import undead

if len(argv) == 1:
    exit("Must Specify A Faction (Fairies, Elven, Angels, "
         "Goblin, Undead, Demon, "
         "Titan, Druid, Faceless, "
         "Mercenary or clickinupgrades)")

if len(argv) == 2:
    # print(argv[1])
    # print(type(argv[1]))
    if argv[1].__str__().lower() == "fairies":
        fairies()
    elif argv[1].__str__().lower() == "elven":
        elven()
    elif argv[1].__str__().lower() == "angels":
        angels()

    elif argv[1].__str__().lower() == "goblin":
        goblin()
    elif argv[1].__str__().lower() == "undead":
        undead()
    elif argv[1].__str__().lower() == "demon":
        demon()

    elif argv[1].__str__().lower() == "titan":
        titan()
    elif argv[1].__str__().lower() == "druid":
        druid()
    elif argv[1].__str__().lower() == "faceless":
        faceless()

    elif argv[1].__str__().lower() == "mercenary":
        mercenary()

    elif argv[1].__str__().lower() == "clickinupgrades":
        clickinupgrades()
    else:
        print("Unknown Faction: {}.".format(argv[1].__str__()))

elif len(argv) > 2:
    exit('Unknown Extra Arguments: {}'.format(argv[2:].__str__()))
