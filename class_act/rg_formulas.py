#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""The Module Has Been Built for the Steam Game 'Realm Grinder'.

Specifically to showcase the some of the formulas in the game.

(WIP)
"""
# https://www.kongregate.com/forums/8945-realm-grinder/topics/509904-based-on-upgrades?page=10
# =============================================================================
from math import floor
from pprint import pprint


class GeneralFormulas(object):
    """Class for GeneralFormulas.

    Attributes:
        arg (TYPE): Description.
    """

    def __init__(self,
                 reincarnation,
                 lineage=0,
                 spell_tiers=1,
                 offtime=0,
                 mana_regen=10,
                 sp_duration=20,
                 sp_cost=200
                 ):
        """Summary.

        Args:
            arg (TYPE): Description.
        """
        super(GeneralFormulas, self).__init__()
        self.name = "General Formulas"
        self.lineage_level = lineage + 0
        self.reincarnation = reincarnation + 0
        self.research_points = self.research(self.reincarnation)
        self.offtime = offtime + 0
        self.mana_regen = mana_regen + 0
        self.sp_duration = sp_duration + 0
        self.mana_regen = mana_regen + 0

    def research(self, reincarnation):
        """What Research Points You Can have at your Reincarnation.

        Args:
            reincarnation (TYPE): Description.

        Returns:
            TYPE: Description.
        """
        self.reincarnation = reincarnation
        research_points = (self.reincarnation) * (self.reincarnation + 1) // 2
        print("R {} Research Points: {}".format(self.reincarnation,
                                                research_points))
        return research_points

    def offline_bonus_spell(self, maxmana, reincarnation, tier):
        """Offline bonus for spell tier.

        Args:
            maxmana (TYPE): Description.
            reincarnation (TYPE): Description.
            tier (TYPE): Description.

        Returns:
            TYPE: Description.
        """
        offline_bonus = ((maxmana + 100 * self.reincarnation)**(1 +
                                                                0.15 *
                                                                tier))
        return ("{:.2e}".format(offline_bonus))

    def offline_sp_cast_time(self):
        """Offline Activity Time Gain Formula.

        http://musicfamily.org/realm/Spells/

        Args:
            offtime (TYPE): Description.
            mana_regen (TYPE): Description.
            sp_duration (TYPE): Description.
            sp_cost (TYPE): Description.
            spell_tiers (TYPE): Description.

        Returns:
            TYPE: Description.
        """
        offline_spell_time = self.offtime * min(1, self.mana_regen *
                                                self.sp_duration
                                                (self.spell_tiers *
                                                 self.sp_cost ** 1.5))
        offline_spell_time2 = self.offtime * floor(self.mana_regen *
                                                   self.sp_duration
                                                   (self.spell_tiers *
                                                    self.sp_cost ** 1.5))
        return offline_spell_time, offline_spell_time2


class Goblin(object):
    """Goblin Faction.

    Attributes:
        factioncoin (int): Description.
        lineage_level (int): Description.
        name (str): Description.
    """

    def __init__(self, lineage):
        """Goblin Faction Init."""
        super(Goblin, self).__init__()
        self.name = "Goblin"
        self.lineage_level = lineage + 0
        self.factioncoin = 0

    def goblins_greed(self, lineage, factioncoin):
        """Spell Effect: Increase the production of all buildings.

        Args:
            lineage (TYPE): Description.
            factioncoin (TYPE): Description.

        Returns:
            TYPE: Description.
        """
        formula = ('FC: floor(ln3(1 + x)) + 20, x is gems '
                   'Effect: 0.75 * ln3.15(1 + x)%, x is faction coins found')
        answer = floor((self.lineage_level ** 3) * (1 + self.factioncoin) + 20)
        print("Goblin's Greed Formula: {}".format(formula))
        print("Goblin's Greed  : {0:.3E}".format(answer))
        return answer

    def strong_currency(self, factioncoin):
        """Effect: Increase the production of all buildings.

        Based on the amount of Goblin Coins found in this game.

        Args:
            factioncoin (TYPE): Description.

        Returns:
            TYPE: Description.
        """
        formula = '(1 + factioncoin) ** 0.03'
        answer = (1 + factioncoin) ** 0.03
        print("Increase production of all buildings: {}".format(answer))
        print("Strong Currency Formula: {}".format(formula))
        print("Strong Currency: {0:.3E}".format(answer))
        return answer

    def goblins_economists(self, upgradespurchased):
        """Effect: Increase the production of all buildings:.

                   based on upgrades purchased.

        Formula: x **1.2%, where x is your Upgrades Purchased (This Game) stat.

        Args:
            upgradespurchased (TYPE): Description.

        Returns:
            TYPE: Description.
        """
        formula = ('Formula: x ** 1.2%, where x is your Upgrades Purchased '
                   '(This Game) stat.')
        answer = (upgradespurchased) ** 1.2
        print("Goblin Economists Formula: {}".format(formula))
        print("Goblin Economists: {0:.3E}".format(answer))
        return answer

    def printaname(self):
        """Goblin Faction Init.

        Returns:
            TYPE: Description.
        """
        print("Faction: {}".format(self.name))
        return self.name

    def main(self):
        """Goblin Faction Init."""
        self.printaname()
        self.strong_currency(1e9)


def veteran_figurine(secondz):
    """PH."""
    x = secondz / 1000000
    print("{} % Chance each time you excavate.".format(round(x * 100, 2)))


veteran_figurine(60)
veteran_figurine(60 * 60 * 3)  # 3 hours for a 1% Chance
veteran_figurine(60 * 60 * 24)  # 24 hours for a 8.64% Chance
veteran_figurine(60 * 60 * 24 * 2)  # (2 days) 48 hours for a 17.28% Chance
veteran_figurine(60 * 60 * 24 * 3)  # (3 days) 72 hours for a 25.92% Chance


def dump(obj):
    """Dumper.

    Args:
        obj (TYPE): Description.
    """
    for attr in dir(obj):
        print("obj.{} = {}".format(attr, getattr(obj, attr)))


if __name__ == "__main__":
    a = GeneralFormulas(10)
    a.research(10)
    a.research(20)
    a.research(30)
    a.research(40)
    a.research(50)
    a.research(60)
    a.research(70)
    a.research(80)
    a.research(82)
    a.research(90)
    a.offline_bonus_spell(182200, 63, 1)
    a.offline_bonus_spell(182200, 63, 2)
    a.offline_bonus_spell(182200, 63, 3)
    a.offline_bonus_spell(182200, 63, 4)
    a.offline_bonus_spell(182200, 63, 5)
    a.offline_bonus_spell(182200, 63, 6)
    a.offline_sp_cast_time(60, 100000, 20, 320, 5)
    a.offline_sp_cast_time(600, 118341, 24, 500, 5)
    b = Goblin()
    b.goblins_greed(lineage=30, factioncoin=2994004)
    b.goblins_greed(31, 4.62e29)
    b.strong_currency(factioncoin=2994004)
    b.strong_currency(4.62e29)
    b.goblins_economists(15)
    print("{}".format(a.__dict__))
    print("{}".format(a.__dict__.keys()))
    print("{}".format(a.__dict__.values()))
    print("{}".format(a.__dir__()))
    print("{}".format(dir(Goblin)))
    print("{}".format(vars(Goblin)))
    print("{}".format(', '.join(i for i in dir(Goblin)
                                if not i.startswith('__'))))
    for att in dir(a):
        print("{} - {}".format(att, getattr(a, att)))
    for att in dir(b):
        print("{} - {}".format(att, getattr(b, att)))
    pprint("{}".format(vars(a)))
    pprint("{}".format(a))
    pprint("{}".format(vars(a)))
    pprint("{}".format(vars(a.element)))
    dump("{}".format(a))
    dump("{}".format(b))
