from typing import Union
import sqlite3

from fastapi import FastAPI

from db.db import create_database, seed_database, get_characters

create_database()
seed_database()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/characters")
def get_all_characters():
    characters = get_characters()
    return characters


@app.get("/characters/{character_id}")
def get_character_by_id(character_id: int):
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
