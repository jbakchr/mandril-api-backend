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
    seed_program_overviews()


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


def seed_program_overviews():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    # Check if database has not been seeded
    sql = "SELECT * FROM program_overviews"

    res = cur.execute(sql)

    if len(res.fetchall()) == 0:
        cur_dir = os.getcwd()

        with open(os.path.join(cur_dir, "data", "program_overviews.json")) as f:
            overviews = json.loads(f.read())

        sql = """
          INSERT INTO program_overviews
          VALUES (:sequence, :time, :overview, :episode_id)
        """

        cur.executemany(sql, overviews)
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


def get_all_episodes():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM episodes")

    result = cur.fetchall()

    con.close()

    episodes = []
    for episode in result:
        episodes.append(
            {"episode_id": episode[0], "season": episode[1], "episode": episode[2]}
        )

    return episodes


def get_episodes_season(season: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"SELECT * FROM episodes WHERE season = {season}"

    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    episodes = []
    for el in result:
        episode = {"episode_id": el[0], "season": el[1], "episode": el[2]}
        episodes.append(episode)

    return episodes


def get_episodes_season_characters(season: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"""
            SELECT
                e.episode_id, e.season, e.episode, c.character_id, c.character_name, c.character_desc
            FROM 
                episodes AS e
            INNER JOIN
                character_episode AS ce
            ON
                e.episode_id = ce.episode_id
            INNER JOIN
                characters AS c
            ON
                ce.character_id = c.character_id
            WHERE
                e.season = {season}
        """

    cur.execute(sql)

    result = cur.fetchall()

    episodes = []
    for el in result:
        episode = {
            "episode_id": el[0],
            "season": el[1],
            "episode": el[2],
            "character_id": el[3],
            "character_name": el[4],
            "character_desc": el[5],
        }
        episodes.append(episode)

    con.close()

    return episodes


def get_episode_by_season(season: int, episode: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"SELECT * FROM episodes WHERE season = {season} AND episode = {episode}"

    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    return {"episode_id": result[0][0], "season": result[0][1], "episode": result[0][2]}


def get_episodes_season_episode_characters(season: int, episode: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"""
            SELECT
                e.episode_id, e.season, e.episode, c.character_id, c.character_name, c.character_desc
            FROM 
                episodes AS e
            INNER JOIN
                character_episode AS ce
            ON
                e.episode_id = ce.episode_id
            INNER JOIN
                characters AS c
            ON
                ce.character_id = c.character_id
            WHERE
                e.season = {season} AND e.episode = {episode}
        """

    cur.execute(sql)

    result = cur.fetchall()

    episodes = []
    for el in result:
        episode = {
            "episode_id": el[0],
            "season": el[1],
            "episode": el[2],
            "character_id": el[3],
            "character_name": el[4],
            "character_desc": el[5],
        }
        episodes.append(episode)

    return episodes


def get_program_overviews():
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM program_overviews")

    result = cur.fetchall()

    con.close()

    overviews = []
    for overview in result:
        overviews.append(
            {
                "sequence": overview[0],
                "time": overview[1],
                "overview": overview[2],
                "episode_id": overview[3],
            }
        )

    return overviews


def get_program_overview_from_episode_id(episode_id: int):
    con = sqlite3.connect("mandril.db")
    cur = con.cursor()

    sql = f"SELECT * FROM program_overviews WHERE episode_id = {episode_id}"

    cur.execute(sql)

    result = cur.fetchall()

    con.close()

    overviews = []

    for overview in result:
        item = {
            "sequence": overview[0],
            "time": overview[1],
            "overview": overview[2],
            "episode_id": overview[3],
        }
        overviews.append(item)

    return overviews
