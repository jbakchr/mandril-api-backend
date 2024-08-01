import os
import sqlite3
import json


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


def seed_database():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    # Check if database has not been seeded
    sql = "SELECT * FROM characters"

    res = cur.execute(sql)

    if len(res.fetchall()) == 0:
        # Get character data
        cur_dir = os.getcwd()

        with open(os.path.join(cur_dir, "data", "characters.json")) as f:
            characters = json.loads(f.read())

        sql = """
          INSERT INTO characters
          VALUES (:character_id, :character_name, :character_desc)
        """

        cur.executemany(sql, characters)

        con.commit()
        con.close()
