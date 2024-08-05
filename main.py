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
    get_episodes_season,
    get_episode_by_season,
    get_episodes_season_characters,
    get_episodes_season_episode_characters,
    get_program_overviews,
    get_program_overview_from_episode_id,
)

create_database()
seed_database()

app = FastAPI()


@app.get("/")
def mandril_api():
    return {
        "velkomst": "Hey hummersuppe .. Velkommen til Mandril API! Dokumentation for dette API kan findes via nedenstående link:",
        "link": "https://mandril-api-backend.onrender.com/docs",
    }


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


@app.get("/episodes")
def get_episodes():
    episodes = get_all_episodes()
    return episodes


@app.get("/episodes/{season}")
def get_episodes_by_season(season: int):
    episodes = get_episodes_season(season)
    return episodes


@app.get("/episodes/{season}/characters")
def get_characters_in_season(season: int):
    episodes = get_episodes_season_characters(season)
    return episodes


@app.get("/episodes/{season}/{episode}")
def get_episodes_by_season_and_episode(seaon: int, episode: int):
    episode = get_episode_by_season(seaon, episode)
    return episode


@app.get("/episodes/{season}/{episode}/characters")
def get_characters_by_season_and_episode(season: int, episode: int):
    episodes = get_episodes_season_episode_characters(season, episode)
    return episodes


@app.get("/program-overviews")
def get_all_program_overviews():
    overviews = get_program_overviews()
    return overviews


@app.get("/program-overviews/{episode_id}")
def get_program_overview_by_episode_id(episode_id: int):
    overviews = get_program_overview_from_episode_id(episode_id)
    return overviews
