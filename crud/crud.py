from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional, Dict
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import databases
import sqlalchemy
import os

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:1234@postgres:5432/chartsdb")

# Set up the database connection
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Create an instance of FastAPI
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])

# Models for input/output
class SongFeatures(BaseModel):
    genre: Optional[str]

class ArtistFeatures(BaseModel):
    type: Optional[str]
    gender: Optional[str]
    country: Optional[str]

class ChartEntry(BaseModel):
    position: int
    song: str
    artist: str
    album: Optional[str]
    duration: Optional[str]
    release_date: Optional[date]
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
    query = """
    SELECT c.date, c.current_rank, s.title, s.album, s.length, s.release_date, 
           a.name as artist_name, a.type as artist_type, a.gender, a.country, a.disambiguation,
           string_agg(DISTINCT g.name, ', ') as genres
    FROM charts c
    JOIN songs s ON c.song_id = s.id
    JOIN artists a ON a.id = s.id
    LEFT JOIN artist_genres ag ON a.id = ag.artist_id
    LEFT JOIN genres g ON ag.genre_id = g.id
    """
    
    if date:
        query += " WHERE c.date = :date"
        values = {"date": date}
    else:
        values = {}
    
    query += " GROUP BY c.date, c.current_rank, s.title, s.album, s.length, s.release_date, a.name, a.type, a.gender, a.country,  a.disambiguation"
    query += " ORDER BY c.date, c.current_rank"
    
    try:
        chart_records = await database.fetch_all(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    charts_by_date = {}
    for record in chart_records:
        chart_date = record['date']
        if chart_date not in charts_by_date:
            charts_by_date[chart_date] = []

        duration_ms = record['length'] if record['length'] is not None else 0
        total_seconds = duration_ms // 1000  # Convert milliseconds to seconds
        minutes, seconds = divmod(total_seconds, 60)
        duration = f"{minutes}:{seconds:02d}" if duration_ms else None
        
        charts_by_date[chart_date].append(ChartEntry(
            position=record['current_rank'],
            song=record['title'],
            artist=record['artist_name'],
            album=record['album'],
            duration=duration,
            release_date=record['release_date'],
            songFeatures=dict(genre=record['disambiguation']),
            artistFeatures=dict(
                type=record['gender'],
                gender=record['gender'],
                country=record['country']
            )
        ))

    return [{"date": d, "charts": {"US": entries}} for d, entries in charts_by_date.items()]

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
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)