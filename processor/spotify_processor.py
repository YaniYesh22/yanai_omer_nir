import json
import time
from musicbrainzngs import musicbrainz, WebServiceError, ResponseError, NetworkError, MusicBrainzError
import boto3
import random  
import time
from datetime import datetime
import databases
import sqlalchemy
from sqlalchemy import insert
import sqlite3
import psycopg2
from psycopg2.extras import Json

DATABASE_URL = "postgres://myuser:1234@postgres:5432/chartsdb"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

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
    sqlalchemy.Column("release_date", sqlalchemy.Date)
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

# Configure MusicBrainz API
musicbrainz.set_useragent("MusicDataEnricher", "1.0", "your-email@example.com")
musicbrainz.set_rate_limit(limit_or_interval=1.0, new_requests=1)

def get_artist_info(artist_name, max_retries=25, backoff_factor=1.5):
    for attempt in range(max_retries):
        try:
            result = musicbrainz.search_artists(artist=artist_name, limit=1)
            if result['artist-list']:
                artist = result['artist-list'][0]
                artist_id = artist['id']
                artist_details = musicbrainz.get_artist_by_id(artist_id, includes=['tags', 'recordings', 'releases'])

                genres = [tag['name'] for tag in artist_details['artist'].get('tag-list', [])]

                return {
                    "name": artist_details['artist'].get('name'),
                    "disambiguation": artist_details['artist'].get('disambiguation'),
                    "country": artist_details['artist'].get('country'),
                    "life-span": artist_details['artist'].get('life-span'),
                    "gender": artist_details['artist'].get('gender'),
                    "type": artist_details['artist'].get('type'),
                    "genres": genres,
                    "tags": artist_details['artist'].get('tag-list', []),
                    "recording_count": artist_details['artist'].get('recording-count'),
                    "release_count": artist_details['artist'].get('release-count'),
                }
        except (WebServiceError, ResponseError, NetworkError) as e:
            print(f"Error fetching artist info from MusicBrainz for {artist_name}: {e}")
            if attempt < max_retries - 1:
                sleep_time = (backoff_factor ** attempt) + random.uniform(0, 1)
                print(f"Retrying in {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
            else:
                print(f"Failed to fetch artist info for {artist_name} after {max_retries} attempts.")
                return None
            

def get_song_info(song_name, artist_name, max_retries=25, backoff_factor=1.5):
    for attempt in range(max_retries):
        try:
            result = musicbrainz.search_recordings(recording=song_name, artist=artist_name, limit=1)
            if result['recording-list']:
                recording = result['recording-list'][0]
                return {
                    "title": recording.get('title'),
                    "length": recording.get('length'),
                    "album": recording.get('release-list')[0]['title'] if recording.get('release-list') else None,
                    "tags": recording.get('tag-list', [])
                }
        except (WebServiceError, ResponseError, NetworkError, MusicBrainzError) as e:
            print(f"Error fetching song info from MusicBrainz for {song_name}: {e}")

            # Check if the error is a rate limiting error (HTTP 429)
            if "503" in str(e) or "429" in str(e):
                print(f"Rate limit encountered. Attempt {attempt + 1} of {max_retries}.")

            if attempt < max_retries - 1:
                sleep_time = backoff_factor ** attempt + random.uniform(0, 1)
                print(f"Retrying in {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
            else:
                print(f"Failed to fetch song info for {song_name} after {max_retries} attempts.")
                return None
            

def enrich_data(data):
    enriched_data = {}
    
    for date, songs in data.items():
        enriched_data[date] = []
        for song in songs:
            song_info = get_song_info(song['song_name'], song['artists'][0])
            
            # Process each artist individually
            artists_info = []
            for artist_name in song['artists']:
                artist_info = get_artist_info(artist_name)
                if artist_info:
                    artists_info.append(artist_info)
            
            enriched_song = song.copy()
            enriched_song['song_details'] = song_info
            enriched_song['artist_details'] = artists_info
            
            enriched_data[date].append(enriched_song)
            
            # Respect rate limits
            time.sleep(1)

    return enriched_data

def add_details(event, context):
    print('add_details triggered')

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    print("Connected to PostgreSQL database")

    for record in event['Records']:
        try:
            print("Processing record")
            message_body = json.loads(record['body'])
            
            if isinstance(message_body, str):
                chart_data = json.loads(message_body)
            else:
                chart_data = message_body

            # Enrich the data with additional artist and song details
            enriched_data = enrich_data(chart_data)

            if enriched_data:
                print("Enriched data")

                # Use the first date in the data as the chart date
                chart_date = list(chart_data.keys())[0] if chart_data else "unknown_date"
                output_file = f'/tmp/processed_chart_{chart_date}.json'
                
                # Save to JSON
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(enriched_data, f, indent=2, ensure_ascii=False)

                print(f"Processing complete for {chart_date}. Results saved to '{output_file}'")

                # Insert into the database
                insert_into_db(cursor, enriched_data)

            else:
                print("No processed data generated.")
        except Exception as e:
            print(f"Error processing SQS message: {e}")

    # Commit the transaction and close the connection
    connection.commit()
    cursor.close()
    connection.close()

def insert_into_db(cursor, enriched_data):
    for date, songs in enriched_data.items():
        for song in songs:
            # Insert the song into the songs table
            song_query = """
            INSERT INTO songs (title, length, album, release_date) 
            VALUES (%s, %s, %s, %s) RETURNING id
            """
            cursor.execute(song_query, (
                song['song_name'],
                song['song_details']['length'],
                song['song_details']['album'],
                song['release_date']
            ))
            song_id = cursor.fetchone()[0]

            # Insert artists into the artists table
            for artist_detail in song['artist_details']:
                artist_query = """
                INSERT INTO artists (name, disambiguation, country, life_span, gender, type) 
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id
                """
                cursor.execute(artist_query, (
                    artist_detail['name'],
                    artist_detail.get('disambiguation'),
                    artist_detail.get('country'),
                    Json(artist_detail.get('life-span')),  # Assuming life-span is a dictionary
                    artist_detail.get('gender'),
                    artist_detail.get('type')
                ))
                artist_id = cursor.fetchone()[0]

            # Insert the chart record into the charts table
            chart_query = """
            INSERT INTO charts (date, song_id, current_rank) 
            VALUES (%s, %s, %s)
            """
            cursor.execute(chart_query, (
                date,
                song_id,
                song['current_rank']
            ))
        print(f'Data inserted to {date}')
