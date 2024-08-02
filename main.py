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
    get_actor_by_actor_id,
    get_character_actor,
    get_actor_characters,
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


@app.get("/characters/{character_id}/actors")
def character_played_by_actors(character_id: int):
    character_played_by_actors = get_character_actor(character_id)
    return character_played_by_actors


@app.get("/actors")
def get_all_actors():
    actors = get_actors()
    return actors


@app.get("/actors/{id}")
def get_actor_by_id(id: int):
    actor = get_actor_by_actor_id(id)
    return actor


@app.get("/actors/{id}/characters")
def actor_plays_characters(id: int):
    actor_characters = get_actor_characters(id)
    return actor_characters
