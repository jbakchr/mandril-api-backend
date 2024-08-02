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
    seed_characters()
    seed_actors()
    seed_character_actor()
    seed_episodes()
    seed_character_episode()


def seed_characters():
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


def seed_actors():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    # Check if database has not been seeded
    sql = "SELECT * FROM actors"

    res = cur.execute(sql)

    if len(res.fetchall()) == 0:
        cur_dir = os.getcwd()

        with open(os.path.join(cur_dir, "data", "actors.json")) as f:
            actors = json.loads(f.read())

        sql = """
          INSERT INTO actors
          VALUES (:actor_id, :actor_name)
        """

        cur.executemany(sql, actors)
        con.commit()

    con.close()


def seed_character_actor():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    # Check if database has not been seeded
    sql = "SELECT * FROM character_actor"

    res = cur.execute(sql)

    if len(res.fetchall()) == 0:
        cur_dir = os.getcwd()

        with open(os.path.join(cur_dir, "data", "character_actor.json")) as f:
            data = json.loads(f.read())

        sql = """
          INSERT INTO 
            character_actor
          VALUES 
            (:character_id, :actor_id)
        """

        cur.executemany(sql, data)
        con.commit()

    con.close()


def seed_episodes():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    # Check if database has not been seeded
    sql = "SELECT * FROM episodes"

    res = cur.execute(sql)

    if len(res.fetchall()) == 0:
        cur_dir = os.getcwd()

        with open(os.path.join(cur_dir, "data", "episodes.json")) as f:
            episodes = json.loads(f.read())

        sql = """
          INSERT INTO episodes
          VALUES (:episode_id, :season, :episode)
        """

        cur.executemany(sql, episodes)
        con.commit()

    con.close()


def seed_character_episode():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    # Check if database has not been seeded
    sql = "SELECT * FROM character_episode"

    res = cur.execute(sql)

    if len(res.fetchall()) == 0:
        cur_dir = os.getcwd()

        with open(os.path.join(cur_dir, "data", "character_episode.json")) as f:
            data = json.loads(f.read())

        sql = """
          INSERT INTO 
            character_episode
          VALUES 
            (:character_id, :episode_id)
        """

        cur.executemany(sql, data)
        con.commit()

    con.close()


def get_characters():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM characters")

    characters = cur.fetchall()

    con.close()

    res_json = []
    for character in characters:
        item = {
            "character_id": character[0],
            "character_name": character[1],
            "character_desc": character[2],
        }
        res_json.append(item)

    return res_json


def get_character_by_character_id(character_id: int) -> dict:
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"SELECT * FROM characters WHERE character_id = {int(character_id)}"

    cur.execute(sql)

    res = cur.fetchall()

    con.close()

    character = None
    for value in res:
        character = {
            "character_id": value[0],
            "character_name": value[1],
            "character_desc": value[2],
        }

    return character


def get_character_actor(character_id: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"""
            SELECT
                c.character_id, c.character_name, c.character_desc, a.actor_id, a.actor_name
            FROM
                characters AS c
            INNER JOIN
                character_actor AS ca
            ON
                c.character_id = ca.character_id
            INNER JOIN
                actors AS a
            ON
                ca.actor_id = a.actor_id
            WHERE
                c.character_id = {character_id}
        """

    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    character_actor = {
        "character_id": character_id,
        "character_name": "",
        "character_desc": "",
        "actors": [],
    }

    for el in result:
        character_actor["character_name"] = el[1]
        character_actor["character_desc"] = el[2]

        actor = {"actor_id": el[3], "actor_name": el[4]}
        character_actor["actors"].append(actor)

    return character_actor


def get_actors():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM actors")

    result = cur.fetchall()

    con.close()

    actors = []
    for actor in result:
        actors.append({"actor_id": actor[0], "actor_name": actor[1]})

    return actors


def get_actor_by_actor_id(actor_id: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"SELECT * FROM actors WHERE actor_id = {int(actor_id)}"

    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    actor = None
    for value in result:
        actor = {"actor_id": value[0], "actor_name": value[1]}

    return actor


def get_actor_characters(actor_id: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"""
            SELECT
                a.actor_id, a.actor_name, c.character_id, c.character_name
            FROM
                actors AS a
            INNER JOIN
                character_actor AS ca
            ON
                a.actor_id = ca.actor_id
            INNER JOIN
                characters AS c
            ON
                ca.character_id = c.character_id
            WHERE
                a.actor_id = {actor_id}
    """

    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    actor_characters = {"actor_id": actor_id, "actor_name": "", "characters": []}

    for el in result:
        actor_characters["actor_name"] = el[1]

        character = {"character_id": el[2], "character_name": el[3]}
        actor_characters["characters"].append(character)

    return actor_characters
