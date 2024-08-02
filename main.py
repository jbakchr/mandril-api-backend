from typing import Union
import sqlite3

from fastapi import FastAPI

from db.db import (
    create_database,
    seed_database,
    get_characters,
    get_character_by_character_id,
)

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
    character = get_character_by_character_id(character_id)
    return character
