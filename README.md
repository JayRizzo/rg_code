# Realm Grinder Code (Python3)
This is a Collection of Random Creations used for the Desktop game 'Realm Grinder'

# Requirements
- Python3 (currently using `Python 3.7.4`)
- pyautogui.__version__ '0.9.44' 

# Setup
- `pip3 install 'pyautogui==0.9.44' --force --upgrade`

This code has been my side project for some time as I really like the game "Realm Grinder" and have been inspired to take a different approach as the clicker game has made me go thru batteries and mice like crazy.   

So, to learn some things in the process i have created these:

* `runnindown.py` has been built as an independant isolated module
* `Core.py` is has been built to have independant parts that interact together.  The `Core.py` has been built to determine the screen size of the laptop or connected devices. 

Call the `Core.py` file like so:
#### Must Specify A Faction (Fairies, Elven, Angels, Goblin, Undead, Demon, Titan, Druid, Faceless, Mercenary or clickinupgrades).


    python3 ~/your_path/class_act/Core.py Fairies
    python3 ~/your_path/class_act/Core.py Elven
    python3 ~/your_path/class_act/Core.py Angels

    python3 ~/your_path/class_act/Core.py Goblin
    python3 ~/your_path/class_act/Core.py Undead
    python3 ~/your_path/class_act/Core.py Demon

    python3 ~/your_path/class_act/Core.py Titan
    python3 ~/your_path/class_act/Core.py Druid
    python3 ~/your_path/class_act/Core.py Faceless

    python3 ~/your_path/class_act/Core.py Mercenary ( this moves the marker for the location of the buyall button )
    python3 ~/your_path/class_act/Core.py clickinupgrades  ( this only buys upgrades and make money )

* `faction_research.md` is my log on all the different ways I have used to play the game for research and mercenaries go.  (in game verbiage)

