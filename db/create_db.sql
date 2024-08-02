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