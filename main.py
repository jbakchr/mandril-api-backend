from typing import Union
import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/characters")
def read_item():
    with open("./characters.json") as f:
        characters = json.loads(f.read())
    return characters
