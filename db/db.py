import os
import sqlite3


def create_database():

    # Read script to create tables
    cur_dir = os.getcwd()

    with open(os.path.join(cur_dir, "db", "create_db.sql")) as f:
        script = f.read()

    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    cur.executescript(script)

    con.commit()
    con.close()
