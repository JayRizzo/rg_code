#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module Has Been Built for the Steam Game 'Realm Grinder'.

Direction: To create a random build regardless of reincarnation level.

Inspired by http://musicfamily.org/realm/SpecialBuilds/
https://github.com/G00FBALL/not-a-wiki/commit/8252ba8e0ff345c2fcacee8820e3d826402a5ec0
https://www.kongregate.com/forums/8945/topics/1628696?page=1

Listing of all Options.
https://www.kongregate.com/forums/8945-realm-grinder/topics/922600-3-0-build-megathread-under-construction-please-post-builds-to-add?page=1
https://www.kongregate.com/forums/8945/topics/1628696?page=1

# FC1  -- Fairy
# EL1  -- Elven
# AN1  -- Angel

# GB1  -- Goblin
# UD1  -- Undead
# DM1  -- Demon

# TT1  -- Titan
# DD1  -- Druid
# FR1  -- Faceless

# DN1  -- Dwarven
# DW1  -- Drow
# DG1  -- Dragon

# MA:FR9  -- Extra Good Choice Mercenary Spell
# MA:GB9  -- Extra Evil Choice Mercenary Spell
# MA:DG9  -- Extra Neutral Choice Mercenary Spell
"""
# =============================================================================

import re

from random import choice


def research(reincarnation):
    """How Many Research Points You Can Have At Your Reincarnation."""
    reincarnation = reincarnation.__str__()
    reincarnation = re.sub(r"\D", "", reincarnation)
    research_points = (int(reincarnation)) * (int(reincarnation) + 1) // 2
    print("For 'R{}' Your Current Research Points: {}".format(reincarnation,
                                                              research_points))
    return research_points


def restrictions_game_env(landscape, faction, reincarnationz):
    """Listing of Research Options Restricted To Landscape."""
    land = landscape
    if land.title() == 'Good':
        print("Landscape: {}".format(land.title()))
        print("Faction: {}".format(faction.title()))
        research(reincarnationz)
    if land.title() == 'Evil':
        print("Landscape: {}".format(land.title()))
        print("Faction: {}".format(faction.title()))
        research(reincarnationz)
    if land.title() == 'Neutral':
        print("Landscape: {}".format(land.title()))
        print("Faction: {}".format(faction.title()))
        research(reincarnationz)
    return


def research_setup():
    """Listing of all Research Options.

    Has Leading ZERO's for sorting purposes.
    """
    # SpellCraft (Fairies) (Good)
    s = ['S0001', 'S0010', 'S0030', 'S0050', 'S0105', 'S0135', 'S0150',
         'S0175', 'S0180', 'S0200', 'S0215', 'S0225', 'S0250', 'S0251',
         'S0270', 'S0300', 'S0305', 'S0330', 'S0375', 'S0400', 'S0435',
         'S0460', 'S0500', 'S0545', 'S0590', 'S1275', 'S1450', 'S1500',
         'S2875', 'S3200',
         ]
    # Craftsman (Elven) (Good)
    c = ['C0001', 'C0010', 'C0025', 'C0050', 'C0080', 'C0105', 'C0120',
         'C0135', 'C0150', 'C0175', 'C0200', 'C0225', 'C0250', 'C0251',
         'C0300', 'C0305', 'C0330', 'C0340', 'C0375', 'C0400', 'C0405',
         'C0460', 'C0500', 'C0520', 'C0590', 'C1300', 'C1325', 'C1500',
         'C3000', 'C3100',
         ]
    # Divine (Angels) (Good)
    d = ['D0001', 'D0010', 'D0025', 'D0050', 'D0055', 'D0135', 'D0150',
         'D0175', 'D0200', 'D0205', 'D0225', 'D0245', 'D0250', 'D0260',
         'D0275', 'D0290', 'D0320', 'D0330', 'D0350', 'D0400', 'D0435',
         'D0480', 'D0525', 'D0560', 'D0590', 'D1125', 'D1275', 'D1375',
         'D2775',
         ]
    # Econiomics (Goblins) (Evil)
    e = ['E0001', 'E0010', 'E0025', 'E0030', 'E0050', 'E0080', 'E0135',
         'E0145', 'E0150', 'E0200', 'E0225', 'E0230', 'E0250', 'E0260',
         'E0275', 'E0290', 'E0320', 'E0330', 'E0350', 'E0400', 'E0410',
         'E0460', 'E0480', 'E0495', 'E0590', 'E1225', 'E1325', 'E1425',
         'E1425', 'E3250', 'E3300',
         ]
    # Alchemy (Undead) (Evil)
    a = ['A0001', 'A0010', 'A0025', 'A0030', 'A0050', 'A0055', 'A0105',
         'A0120', 'A0135', 'A0150', 'A0175', 'A0200', 'A0250', 'A0251',
         'A0270', 'A0300', 'A0305', 'A0330', 'A0375', 'A0400', 'A0410',
         'A0480', 'A0495', 'A0545', 'A0590', 'A1200', 'A1325', 'A1500',
         'A2950', 'A3400',
         ]
    # Warfare (Deamons) (Evil)
    w = ['W0001', 'W0010', 'W0025', 'W0050', 'W0120', 'W0135', 'W0150',
         'W0175', 'W0180', 'W0200', 'W0205', 'W0225', 'W0250', 'W0260',
         'W0275', 'W0290', 'W0320', 'W0330', 'W0350', 'W0400', 'W0405',
         'W0520', 'W0525', 'W0560', 'W0590', 'W1275', 'W1375', 'W1400',
         'W3050', 'W3150',
         ]
    all_good = list(set(s + c + d))
    all_evil = list(set(e + a + w))
    all_research = list(set(all_good + all_evil))
    all_clean_research = clean_import(all_research)
    return all_clean_research


def mercenary_setup():
    """Listing of all Mercenary Options."""
    # Good Factions
    merc_fairyz = ['FC1', 'FC2', 'FC3',
                   'FC4', 'FC5', 'FC6',
                   'FC7', 'FC8', 'FC9']
    merc_elvenz = ['EL1', 'EL2', 'EL3',
                   'EL4', 'EL5', 'EL6',
                   'EL7', 'EL8', 'EL9']
    merc_angelz = ['AN1', 'AN2', 'AN3',
                   'AN4', 'AN5', 'AN6',
                   'AN7', 'AN8', 'AN9']
    # Evil Factions
    merc_goblin = ['GB1', 'GB2', 'GB3',
                   'GB4', 'GB5', 'GB6',
                   'GB7', 'GB8', 'GB9']
    merc_undead = ['UD1', 'UD2', 'UD3',
                   'UD4', 'UD5', 'UD6',
                   'UD7', 'UD8', 'UD9']
    merc_demons = ['DM1', 'DM2', 'DM3',
                   'DM4', 'DM5', 'DM6',
                   'DM7', 'DM8', 'DM9']
    # Neutral Factions
    merc_titans = ['TT1', 'TT2', 'TT3',
                   'TT4', 'TT5', 'TT6',
                   'TT7', 'TT8', 'TT9']
    merc_druids = ['DD1', 'DD2', 'DD3',
                   'DD4', 'DD5', 'DD6',
                   'DD7', 'DD8', 'DD9']
    merc_facels = ['FR1', 'FR2', 'FR3',
                   'FR4', 'FR5', 'FR6',
                   'FR7', 'FR8', 'FR9']
    all_mercz = list(set(merc_fairyz + merc_elvenz + merc_angelz +
                         merc_goblin + merc_undead + merc_demons +
                         merc_titans + merc_druids + merc_facels
                         )
                     )
    all_mercz.sort()
    return all_mercz


def merc_spells():
    """Mercenary Spells."""
    merc_spellz = ["SP:Fairy Chanting",  # Good
                   "SP:Moon Blessing",  # Good
                   "SP:God's Hand",  # Good
                   "SP:Goblin's Greed",  # Evil
                   "SP:Night Time",  # Evil
                   "SP:Hellfire Blast",  # Evil
                   "SP:Lightning Strike",  # Neutral
                   "SP:Grand Balance",  # Neutral
                   "SP:Brainwave",  # Neutral
                   "SP:Diamond Pickaxe",  # Good
                   "SP:Combo Strike",  # Evil
                   "SP:Dragon's Breath",  # Neutral
                   ]
    merc_spellz.sort()
    return merc_spellz


def clean_import(research_clean):
    """Clean Leading Zeros from Researches After the first letter."""
    clean_list = []
    for item in research_clean:
        regex = re.compile('[SCDEAW]')
        a = item
        b = regex.split(a)
        if b[1][0] == '0':
            c = int(b[1])
            d = a[0][0] + str(c)
            clean_list.append(d)
    return clean_list


# def adjust_for_rc(reincarnation):
#     """Clean Leading Zeros from Researches After the first letter."""
#     clean_list = []
#     for item in research_clean:
#         regex = re.compile('[SCDEAW]')
#         a = item
#         b = regex.split(a)
#         if b[1][0] == '0':
#             c = int(b[1])
#             d = a[0][0] + str(c)
#             if c <= research(reincarnation):
#                 clean_list.append(d)
#             else:
#                 pass
#     return clean_list


def randomize_stuff(list_of_things):
    """randomize_stuff."""
    random_list = []
    for _ in range(300):
        random_list.append(choice(list_of_things))
        random_list.sort()
    print("Random Build: {}".format(random_list))
    return random_list


def merc_build(list_of_things, spellz, list_of_research):
    """Random merc_build."""
    random_list = []
    for _ in range(120):
        random_list.append(choice(list_of_things))
    random_list.append(choice(spellz))
    random_list.append(choice(spellz))
    for _ in range(300):
        random_list.append(choice(list_of_research))
    random_list2 = ",".join(random_list)
    print("Merc Build: {}".format(random_list2))
    return random_list2


def fairy_info():
    """Fairy Tier 1, 2 & 3 Upgrades."""
    # Fairy Tier 1 Upgrades
    print(dict({"FR1": "Pixie Dust Fertilizer", "Effect": "Increase the base production of Farms by +98 and reduce the building cost multiplier.Reduces cost multiplier by 0.035; with no other reductions applying, the multiplier will be 1.115 instead of 1.15."}))  # noqa
    print(dict({"FR2": "Fairy Cuisine", "Effect": "Increase the base production of Inns by +234 and reduce the building cost multiplier.Reduces cost multiplier by 0.03; with no other reductions applying, the multiplier will be 1.12 instead of 1.15."}))  # noqa
    print(dict({"FR3": "Star-metal Alloys", "Effect": "Increase the base production of Blacksmiths by +580 and reduce the building cost multiplier.Reduces cost multiplier by 0.025; with no other reductions applying, the multiplier will be 1.125 instead of 1.15."}))  # noqa
    # Fairy Tier 2 Upgrades
    print(dict({"FR4": "Fairy Workers", "Effect": "Increase the production of Farms, Inns and Blacksmiths by 15000%."}))  # noqa
    print(dict({"FR5": "Golden Pots", "Effect": "Increase clicking reward by 20% of the production of Farms, Inns and Blacksmiths combined."}))  # noqa
    print(dict({"FR6": "Spell-smith", "Effect": "Blacksmiths also increase your mana regeneration rate.", "Formula": "(x ** 0.25), where x is the number of Blacksmiths you own."}))  # noqa
    # Fairy Tier 3 Upgrades
    print(dict({"FR7": "Kind Hearts", "Effect": "Increases maximum mana by 1 for every 8 good buildings you own."}))  # noqa
    print(dict({"FR8": "Rainbow Link", "Effect": "Increase the production of all buildings by 0.3% per Farm, Inn and Blacksmith you own."}))  # noqa
    print(dict({"FR9": "Swarm of Fairies", "Effect": "You gain additional assistants based on the amount of Farms, Inns and Blacksmiths you own.", "Formula": "floor((sqrt(1+4*x)-1)/3), where x is the number of Farms, Inns, and Blacksmiths you own.", "Reverse Formula": "ceiling(((x * 3 + 1)^ 2-1)/4), where x is the number of Assistants you own."}))  # noqa


def elven_info():
    """Elven Tier 1, 2 & 3 Upgrades."""
    # Elven Tier 1 Upgrades
    print(dict({"EL1": "", "Effect": ""}))  # noqa
    print(dict({"EL2": "", "Effect": ""}))  # noqa
    print(dict({"EL3": "", "Effect": ""}))  # noqa
    # Elven Tier 2 Upgrades
    print(dict({"EL4": "", "Effect": ""}))  # noqa
    print(dict({"EL5": "", "Effect": ""}))  # noqa
    print(dict({"EL6": "", "Effect": ""}))  # noqa
    # Elven Tier 3 Upgrades
    print(dict({"EL7": "", "Effect": ""}))  # noqa
    print(dict({"EL8": "", "Effect": ""}))  # noqa
    print(dict({"EL9": "", "Effect": ""}))  # noqa


if __name__ == '__main__':
    print("")
    merc_build(mercenary_setup(), merc_spells(), research_setup())
