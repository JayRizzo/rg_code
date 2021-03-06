# Realm Grinder Code (Python3)
This Repo is a Collection of Random Creations used for the Desktop game 'Realm Grinder'.

# Requirements
- Mac OSX Mojave 10.14.6 (18G95)
- MacBook Pro (Retina, 15-inch, Mid 2015)
- 2.8 GHz Intel Core i7
- 16 GB 1600 MHz DDR3
- Intel Iris Pro 1536 MB
- Python3 (currently using `Python 3.7.4`)
- pyautogui.__version__ '0.9.44'

# Setup
```bash
    # Jump your terminal to this repo
    cd rg_code
    # Install a virtual environment
    python3 -m venv env
    # Activate this new environment
    source env/bin/activate
    # Install the required packages
    pip3 install 'pyautogui==0.9.44'
    pip install pyobjc
    pip install pyobjc-core
```

This code has been my side project for some time as I really like the game "Realm Grinder" and have been inspired to take a different approach as the clicker game has made me go through batteries and mice like crazy.

So, to learn some things in the process I have created these:

* `Core.py` has been built to independently have moving parts that interact together, making it isolated to determine the screen size of the laptop or connected monitors.

Call the `Core.py` file like so:
#### Must Specify A Faction (Fairy, Elven, Angel, Goblin, Undead, Demon, Titan, Druid, Faceless, Mercenary or clickinupgrades).

```bash
    python3 class_act/Core.py Fairy
    python3 class_act/Core.py Elven
    python3 class_act/Core.py Angel

    python3 class_act/Core.py Goblin
    python3 class_act/Core.py Undead
    python3 class_act/Core.py Demon

    python3 class_act/Core.py Titan
    python3 class_act/Core.py Druid
    python3 class_act/Core.py Faceless

    # This moves the marker for the location of the 'Buy All' button
    python3 class_act/Core.py Mercenary
    python3 class_act/Core.py Mercs
    python3 class_act/Core.py Merc

    # This only buys upgrades and make money
    python3 class_act/Core.py clickinupgrades
    python3 class_act/Core.py mercinupgrades
```

* `faction_research.md` is my log on all the different ways I have used to play the game for research and mercenaries go.  (in game verbiage)

    # 1st Tier
    # 2nd Tier
    # 3rd Tier
    # Spells
       "SP:Fairy Chanting",  # Good
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
       "SP:Dragon's Breath"

    # Spellcraft
    # Craftsmanship
    # Divine
    # Economics
    # Alchemy
    # Warfare


    Specifics
    ### Specific MERCs R75+

    ##### Gem Multiplier
    E495,E400,E460,E30,A250,A105,S460,S330,S105,S30,C175,C340,C500,

    ##### Spell Duration Research
    S200, A270, W1275
    ##### Spell Cost Reduction
    S1275, D200
    ##### Mana Regen
    S30, S105, S500
    ##### MAX Mana
    S30, S105, S400, S500
    #### Offline
    ##### Offline Diamonds
    S435
    ##### Offline Spell Casts
    S50
