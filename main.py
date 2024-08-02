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
    get_all_episodes,
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


@app.get("/actors/{actor_id}")
def get_actor_by_id(actor_id: int):
    actor = get_actor_by_actor_id(actor_id)
    return actor


@app.get("/actors/{actor_id}/characters")
def actor_plays_characters(actor_id: int):
    actor_characters = get_actor_characters(actor_id)
    return actor_characters


@app.get("/episodes")
def get_episodes():
    episodes = get_all_episodes()
    return episodes
