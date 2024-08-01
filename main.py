from typing import Union
import json
import sqlite3

from fastapi import FastAPI

from db.db import create_database, seed_database

create_database()
seed_database()

# con = sqlite3.connect("mandril.db")
# cur = con.cursor()
# res = cur.execute("SELECT * FROM characters")
# for x in res.fetchall():
#     print(x)
# con.close()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/characters")
def read_item():
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
