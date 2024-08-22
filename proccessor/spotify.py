import requests
import base64
import json
import time
from collections import defaultdict

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
    
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    
    response = requests.get(url, headers=headers, params=params)
    search_data = json.loads(response.content)
    
    if search_data['artists']['items']:
        return search_data['artists']['items'][0]
    return None

def get_artist_details(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    artist_data = json.loads(response.content)
    
    return {
        "name": artist_data.get('name', 'Unknown'),
        "genres": artist_data.get('genres', []),
        "popularity": artist_data.get('popularity', 0),
        "followers": artist_data.get('followers', {}).get('total', 0),
        "spotify_url": artist_data.get('external_urls', {}).get('spotify', '')
    }

def process_charts_with_artist_details(charts_data):
    token = get_access_token()
    processed_data = defaultdict(list)

    for date, songs in charts_data.items():
        for song in songs:
            song_with_details = song.copy()
            artists_with_details = []
            for artist_name in song['artists']:
                artist = search_artist(token, artist_name)
                if artist:
                    artist_details = get_artist_details(token, artist['id'])
                    artists_with_details.append(artist_details)
                else:
                    artists_with_details.append({"name": artist_name, "error": "Artist not found"})
                time.sleep(1)  # To avoid rate limiting
            song_with_details['artists'] = artists_with_details
            processed_data[date].append(song_with_details)
        print(f"Processed data for {date}")

    return dict(processed_data)

# Load the existing chart data
with open('processed_all_chart_data.json', 'r', encoding='utf-8') as f:
    charts_data = json.load(f)

# Process the data with artist details
processed_data = process_charts_with_artist_details(charts_data)

# Save the result to a file
with open('processed_charts_with_artist_details.json', 'w', encoding='utf-8') as f:
    json.dump(processed_data, f, indent=2, ensure_ascii=False)

print("Processing complete. Results saved to 'processed_charts_with_artist_details.json'")