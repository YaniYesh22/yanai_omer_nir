from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import date, datetime
import databases
import sqlalchemy
import os
import uvicorn
import json
# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://myuser:1234@localhost:5432/chartsdb")

# Set up the database connection
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Define the tables based on your schema
charts = sqlalchemy.Table(
    "charts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.Date, nullable=False),
    sqlalchemy.Column("song_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("songs.id")),
    sqlalchemy.Column("current_rank", sqlalchemy.Integer)
)

songs = sqlalchemy.Table(
    "songs",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("length", sqlalchemy.Integer),
    sqlalchemy.Column("album", sqlalchemy.String),
    sqlalchemy.Column("release_date", sqlalchemy.Date),
    sqlalchemy.Column("spotify_url", sqlalchemy.String)
)

artists = sqlalchemy.Table(
    "artists",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("disambiguation", sqlalchemy.Text),
    sqlalchemy.Column("country", sqlalchemy.String(3)),
    sqlalchemy.Column("life_span", sqlalchemy.JSON),
    sqlalchemy.Column("gender", sqlalchemy.String(50)),
    sqlalchemy.Column("type", sqlalchemy.String(50))
)

# Create an instance of FastAPI
app = FastAPI()

# Models for input/output
class SongFeatures(BaseModel):
    key: Optional[str]
    genre: Optional[str]
    language: Optional[str]

class ArtistFeatures(BaseModel):
    type: Optional[str]

class ChartEntry(BaseModel):
    position: int
    song: str
    artist: str
    album: Optional[str]
    duration: str
    spotify_url: Optional[str]
    songFeatures: Optional[SongFeatures]
    artistFeatures: Optional[ArtistFeatures]

class ChartResponse(BaseModel):
    date: date
    charts: Dict[str, List[ChartEntry]]

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/charts", response_model=List[ChartResponse])
async def read_charts(date: Optional[date] = Query(None)):
    if date:
        query = """
        SELECT c.date, c.current_rank, s.title, s.album, s.length, s.spotify_url, 
               a.name as artist_name, a.type as artist_type, a.life_span
        FROM charts c
        JOIN songs s ON c.song_id = s.id
        JOIN artists a ON a.id = s.id
        WHERE c.date = :date
        ORDER BY c.date, c.current_rank
        """
        values = {"date": date}
    else:
        query = """
        SELECT c.date, c.current_rank, s.title, s.album, s.length, s.spotify_url, 
               a.name as artist_name, a.type as artist_type, a.life_span
        FROM charts c
        JOIN songs s ON c.song_id = s.id
        JOIN artists a ON a.id = s.id
        ORDER BY c.date, c.current_rank
        """
        values = {}
    
    try:
        chart_records = await database.fetch_all(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    charts_by_date = {}
    for record in chart_records:
        chart_date = record['date']
        if chart_date not in charts_by_date:
            charts_by_date[chart_date] = []

        duration_seconds = record['length'] if record['length'] is not None else 0
        duration = f"{duration_seconds // 60}:{duration_seconds % 60:02d}"
        
        life_span = json.loads(record['life_span']) if record['life_span'] else {}
        
        charts_by_date[chart_date].append(ChartEntry(
            position=record['current_rank'],
            song=record['title'],
            artist=record['artist_name'],
            album=record['album'],
            duration=duration,
            spotify_url=record['spotify_url'],
            songFeatures=SongFeatures(
                key=None,
                genre=None,
                language=None
            ),
            artistFeatures=ArtistFeatures(
                type=record['artist_type']
            )
        ))

    return [ChartResponse(date=d, charts={"US": entries}) for d, entries in charts_by_date.items()]


@app.get("/charts/available-dates")
async def get_available_dates():
    query = "SELECT DISTINCT date FROM charts ORDER BY date"
    dates = await database.fetch_all(query)
    
    date_dict = {}
    for record in dates:
        chart_date = record['date']
        year = str(chart_date.year)
        month = str(chart_date.month).zfill(2)
        day = str(chart_date.day)
        
        if year not in date_dict:
            date_dict[year] = {}
        if month not in date_dict[year]:
            date_dict[year][month] = []
        date_dict[year][month].append(day)
    
    return date_dict

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)