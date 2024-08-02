from typing import Union
import sqlite3
import json

from fastapi import FastAPI

from db.db import (
    create_database,
    seed_database,
    get_characters,
    get_character_by_character_id,
    get_actors,
)

create_database()
seed_database()

app = FastAPI()


@app.get("/characters")
def get_all_characters():
    characters = get_characters()
    return characters


@app.get("/characters/{character_id}")
def get_character_by_id(character_id: int):
    character = get_character_by_character_id(character_id)
    return character


@app.get("/actors")
def get_all_actors():
    actors = get_actors()
    return actors
