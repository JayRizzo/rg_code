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


def research(reincarnation):
    """What Research Points You Can have at your Reincarnation."""
    research_points = (reincarnation) * (reincarnation + 1) // 2
    print("R {} Research Points: {}".format(reincarnation, research_points))
    return research_points

research(10)
research(20)
research(30)
research(40)
research(50)
research(60)
research(70)
research(80)
research(82)
research(90)


class Goblin(object):
    """Goblin Faction."""

    def __init__(self, arg):
        """Goblin Faction Init."""
        super(Goblin, self).__init__()
        self.arg = arg

    def goblins_greed(self, lineage, factioncoin):
        """Spell Effect: Increase the production of all buildings."""
        formula = ('FC: floor(ln3(1 + x)) + 20, x is gems '
                   'Effect: 0.75 * ln3.15(1 + x)%, x is faction coins found')
        answer = floor((lineage ** 3 + (1 + factioncoin) + 20))
        print("Goblin's Greed Formula: {}".format(formula))
        print("Goblin's Greed  : {0:.3E}".format(answer))
        return answer

    def strong_currency(self, factioncoin):
        """Effect: Increase the production of all buildings.

        Based on the amount of Goblin Coins found in this game.
        """
        formula = (1 + factioncoin) ** 0.03
        answer = (1 + factioncoin) ** 0.03
        print("Strong Currency Formula: {}".format(formula))
        print("Strong Currency: {0:.3E}".format(answer))
        return answer

    def goblins_economists(self, upgradespurchased):
        """Effect: Increase the production of all buildings:.

                   based on upgrades purchased.

        Formula: x ^ 1.2%, where x is your Upgrades Purchased (This Game) stat.
        """
        formula = ('Formula: x ^ 1.2%, where x is your Upgrades Purchased '
                   '(This Game) stat.')
        answer = (upgradespurchased) ** 1.2
        print("Goblin Economists Formula: {}".format(formula))
        print("Goblin Economists: {0:.3E}".format(answer))
        return answer


Goblin.goblins_greed(None, 31, 4.62e29)
Goblin.strong_currency(None, 4.62e29)
Goblin.goblins_economists(None, 15)


# python3 ~/GitHubz/rg_code/rg_formulas.py
# R 10 Research Points: 55
# R 20 Research Points: 210
# R 30 Research Points: 465
# R 40 Research Points: 820
# R 50 Research Points: 1275
# R 60 Research Points: 1830
# R 70 Research Points: 2485
# R 80 Research Points: 3240
# R 82 Research Points: 3403
# R 90 Research Points: 4095
# Goblin's Greed Formula: FC: floor(ln3(1 + x)) + 20, x is gems Effect: 0.75 * ln3.15(1 + x)%, x is faction coins found
# Goblin's Greed  : 4.620E+29
# Strong Currency Formula: 7.761385577498356
# Strong Currency: 7.761E+00
# Goblin Economists Formula: Formula: x ^ 1.2%, where x is your Upgrades Purchased (This Game) stat.
# Goblin Economists: 2.578E+01
