#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the visualization."""
# =============================================================================
# from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import Tk
from tkinter import W
import time

TITLE = 'Realm Grinder Clicker'
FOREGROUND = 'Steel Blue'
BACKGROUND = 'Black'
TITLE_FONT = tuple(('aria', 30, 'bold'))
BUTTON_FONT = tuple(('Helvetica', 12))


class Application(Frame):
    """PH."""

    def __init__(self, master):
        """PH."""
        super().__init__(master)
        self.master = master
        master.title(TITLE)  # TITLE BAR
        # master.configure(background='Grey')  # same as below
        master["bg"] = "Grey"

    def current_time(self):
        """PH."""
        localtime = time.asctime(time.localtime(time.time()))
        return localtime

    def window_positioning(self):
        """PH."""
        self.w = 840  # width for the window
        self.h = 1000  # Full Height for the window
        # get screen width and height
        self.ws = self.winfo_screenwidth()  # width of the screen
        self.hs = self.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        self.x = (self.ws / 2) + (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)
        # set the dimensions of the screen and where it is placed
        self.master.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

    def header_row(self):
        """HEADER ROW."""
        info_label = Label(self.master, font=TITLE_FONT,
                           text=TITLE,
                           fg=FOREGROUND,
                           bd=10)
        info_label.grid(row=0, column=1)
        info_label = Label(self.master,
                           text=self.current_time(),
                           font=BUTTON_FONT,
                           fg=FOREGROUND,
                           bg=BACKGROUND)
        info_label.grid(row=1, column=1)
        info_label.configure(anchor="center")

    def faction_button(self):
        """Single Button Dropdown."""
        self.faction_options = ["Fairy (FC)",  # Good
                                "Elven (EL)",  # Good
                                "Angel (AN)",  # Good

                                "Goblin (GB)",  # Evil
                                "Undead (UD)",  # Evil
                                "Demon (DM)",  # Evil

                                "Titan (TT)",  # Neutral
                                "Druid (DD)",  # Neutral
                                "Faceless (FR)",  # Neutral

                                "Dwarven (DN)",  # Good
                                "Drow (DW)",  # Evil
                                "Dragon (DG)",  # Neutral
                                ]

        self.faction_label = Label(self.master, text="Faction:",
                                   font=BUTTON_FONT,
                                   activebackground='Black',
                                   pady=20,
                                   width=10)
        self.faction_label.grid(row=3, column=0, sticky=W)
        self.faction_text = StringVar(self.master)
        self.faction_text.set(self.faction_options[0])  # default value
        self.faction_selection = OptionMenu(self.master,
                                            self.faction_text,
                                            *self.faction_options)
        self.faction_selection.config(width=20,
                                      font=('Helvetica', 12),
                                      activebackground='BLACK'
                                      )
        self.faction_selection["menu"].config(bg="BLUE")
        self.faction_selection.pack()
        self.faction_selection.grid(row=3, column=1)

    def faction_spell_button(self):
        """Single Button Dropdown."""
        self.faction_spell_opts = ["SP:Fairy Chanting",  # Good
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
        self.faction_spell_label = Label(self.master, text="Faction Spell:",
                                         font=('bold', 14), pady=20,
                                         width=10)
        self.faction_spell_label.grid(row=4, column=0, sticky=W)
        self.faction_spell_text = StringVar(self.master)
        self.faction_spell_text.set(self.faction_spell_opts[0])
        self.faction_spell_text.trace("w", self.faction_spell_text)
        self.faction_merc_spell_selection = OptionMenu(self.master,
                                                       self.faction_spell_text,
                                                       *self.faction_spell_opts
                                                       )
        self.faction_merc_spell_selection["menu"].config(bg="GREEN")
        self.faction_merc_spell_selection.pack()
        self.faction_merc_spell_selection.grid(row=4, column=1)


root = Tk()
app = Application(master=root)
app.window_positioning()
app.header_row()
app.faction_button()
app.faction_spell_button()
app.mainloop()
app.Show()

# references
# http://effbot.org/tkinterbook/listbox.htm
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
