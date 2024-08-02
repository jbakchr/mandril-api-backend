CREATE TABLE IF NOT EXISTS characters
(
  character_id INTEGER NOT NULL,
  character_name TEXT NOT NULL,
  character_desc TEXT NOT NULL,
  PRIMARY KEY (character_id)
);

CREATE TABLE IF NOT EXISTS actors
(
  actor_id INTEGER NOT NULL,
  actor_name TEXT NOT NULL,
  PRIMARY KEY (actor_id)
);

CREATE TABLE IF NOT EXISTS character_actor
(
  character_id INTEGER NOT NULL,
  actor_id INTEGER NOT NULL,
  FOREIGN KEY (character_id) REFERENCES characters(character_id),
  FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
);

CREATE TABLE IF NOT EXISTS episodes
(
  episode_id INTEGER NOT NULL,
  season INTEGER NOT NULL,
  episode INTEGER NOT NULL,
  PRIMARY KEY (episode_id)
);