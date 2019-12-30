#!/bin/bash
# -*- coding: utf-8 -*-
"""Testing SQLlite."""
# =============================================================================

import sqlite3 as sqlite
import sys

con = None


def test_sqlite(db):
    """Testing SQLlite."""
    try:
        con = sqlite.connect(db)
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION();')
        data = cur.fetchone()[0]
        print("SQLite Version: {data}".format(data=data))
    except sqlite.Error as e:
        print("Error {}".format(e.args[0]))
        sys.exit(1)
    finally:
        if con:
            con.close()

test_sqlite('rg.db')

# >>> test_sqlite('rg.db')
# SQLite version: 3.29.0
