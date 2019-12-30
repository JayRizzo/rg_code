#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
"""This Module Has Been Build for the log storage for Realm Grinder Clicks."""
# =============================================================================
import sqlite3


class Database:
    """PH."""

    def __init__(self, db):
        """PH."""
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS rg_log ("
                         "id INTEGER PRIMARY KEY, "
                         "faction TEXT, "
                         "clicks INTEGER, "
                         "reincarnation INTEGER, "
                         "buildings INTEGER)"
                         )
        self.conn.commit()

    def fetch(self):
        """PH."""
        self.cur.execute("SELECT * FROM rg_log;")
        rows = self.cur.fetchall()
        return rows

    def insert(self, faction, clicks, reincarnation, buildings):
        """PH."""
        self.cur.execute("INSERT INTO rg_log VALUES (NULL, {}, {}, {}, {})"
                         "".format(faction, clicks, reincarnation, buildings))
        self.conn.commit()

    def remove(self, id):
        """PH."""
        self.cur.execute("DELETE FROM rg_log WHERE id={}".format(id))
        self.conn.commit()

    def update(self, id, faction, clicks, reincarnation, buildings):
        """PH."""
        buildings = float(self.buildings)
        self.cur.execute(("UPDATE rg_log "
                          "SET faction = {}, "
                          "clicks = {}, "
                          "reincarnation = {}, "
                          "buildings = {} "
                          "WHERE id = {}"
                          "".format(faction,
                                    clicks,
                                    reincarnation,
                                    buildings,
                                    id)))
        self.conn.commit()

    def __del__(self):
        """PH."""
        self.conn.close()

# db = Database('rg_logz.db')
