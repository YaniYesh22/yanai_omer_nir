import requests
import base64
import json
import time
from collections import defaultdict
import boto3
import os
import gzip

# Spotify API credentials
CLIENT_ID = '80dbd3be02894ebfb4aabcc28081dc79'
CLIENT_SECRET = 'd469c99ab4d44d008d2d844e929677b2'

def get_access_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    
    try:
        result = requests.post(url, headers=headers, data=data)
        result.raise_for_status()  # Raise an exception for HTTP errors
        json_result = result.json()
        token = json_result["access_token"]
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining access token: {e}")
        return None

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        search_data = response.json()
        if search_data.get('artists', {}).get('items'):
            return search_data['artists']['items'][0]
        else:
            print(f"No artist found for '{artist_name}'")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to search for artist '{artist_name}': {e}")
        return None

def get_artist_details(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        artist_data = response.json()
        
        return {
            "name": artist_data.get('name', 'Unknown'),
            "genres": artist_data.get('genres', []),
            "popularity": artist_data.get('popularity', 0),
            "followers": artist_data.get('followers', {}).get('total', 0),
            "image_url": artist_data.get('images', [{}])[0].get('url', ''),
            "spotify_url": artist_data.get('external_urls', {}).get('spotify', '')
        }
    except requests.exceptions.RequestException as e:
        print(f"Failed to get details for artist ID '{artist_id}': {e}")
        return None

def get_track_details(token, track_name):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": track_name,
        "type": "track",
        "limit": 1
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        track_data = response.json()
        if track_data.get('tracks', {}).get('items'):
            track = track_data['tracks']['items'][0]
            return {
                "length": track.get('duration_ms', 0),
                "track_url": track.get('external_urls', {}).get('spotify', ''),
                "album_name": track['album'].get('name', ''),
                "release_date": track['album'].get('release_date', ''),
                "popularity": track.get('popularity', 0)
            }
        else:
            print(f"No track found for '{track_name}'")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to search for track '{track_name}': {e}")
        return None

def process_charts_with_artist_details(charts_data):
    token = get_access_token()
    if not token:
        print("Failed to obtain Spotify access token.")
        return {}
    
    processed_data = defaultdict(list)

    for date, songs in charts_data.items():
        for song in songs:
            song_with_details = song.copy()
            track_details = get_track_details(token, song['song_name'])

            if track_details:
                song_with_details.update(track_details)

            artists_with_details = []
            for artist_name in song['artists']:
                artist = search_artist(token, artist_name)
                if artist:
                    artist_details = get_artist_details(token, artist['id'])
                    if artist_details:
                        artists_with_details.append(artist_details)
                else:
                    artists_with_details.append({"name": artist_name, "error": "Artist not found"})
                time.sleep(1)  # To avoid rate limiting
            song_with_details['artists'] = artists_with_details
            processed_data[date].append(song_with_details)
        print(f"Processed data for {date}")

    return dict(processed_data)

def add_details(event, context):
    print("add_details triggered")
    for record in event['Records']:
        try:
            print(f"Processing record: {record}")
            message_body = json.loads(record['body'])
            compressed_message = message_body.get('MessageBody', '')
            decompressed_message = decompress_message(compressed_message)
            chart_data = json.loads(decompressed_message)

            # Process the data with artist and track details
            processed_data = process_charts_with_artist_details(chart_data)
            if processed_data:
                print(f"Processed data: {json.dumps(processed_data, indent=2)}")

                # Optionally, save the result to a file
                chart_date = chart_data.get("chart_date", "unknown_date")
                with open(f'/tmp/processed_chart_{chart_date}.json', 'w', encoding='utf-8') as f:
                    json.dump(processed_data, f, indent=2, ensure_ascii=False)

                print(f"Processing complete for {chart_date}. Results saved to '/tmp/processed_chart_{chart_date}.json'")
            else:
                print("No processed data generated.")
        except Exception as e:
            print(f"Error processing SQS message: {e}")

def decompress_message(compressed_message):
    try:
        compressed_bytes = base64.b64decode(compressed_message)
        decompressed_bytes = gzip.decompress(compressed_bytes)
        return decompressed_bytes.decode('utf-8')
    except Exception as e:
        print(f"Error decompressing message: {e}")
        return ""

# if __name__ == "__main__":
#     counter = 0
#     while(True):
#         counter+=1