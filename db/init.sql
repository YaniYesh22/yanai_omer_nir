CREATE TABLE IF NOT EXISTS genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    count INTEGER
);

CREATE TABLE IF NOT EXISTS artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    disambiguation TEXT,
    country VARCHAR(3),
    life_span JSONB,
    gender VARCHAR(50),
    type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS artist_genres (
    artist_id INTEGER REFERENCES artists(id) ON DELETE CASCADE,
    genre_id INTEGER REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY (artist_id, genre_id)
);

CREATE TABLE IF NOT EXISTS artist_tags (
    artist_id INTEGER REFERENCES artists(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (artist_id, tag_id)
);

CREATE TABLE IF NOT EXISTS songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    length INTEGER,
    album VARCHAR(255),
    release_date DATE
);

CREATE TABLE IF NOT EXISTS charts (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    song_id INTEGER REFERENCES songs(id) ON DELETE CASCADE,
    current_rank INTEGER
);

CREATE INDEX IF NOT EXISTS idx_charts_date ON charts(date);
