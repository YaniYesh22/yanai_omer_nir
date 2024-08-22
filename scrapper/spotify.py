import requests
from datetime import datetime, timedelta
import json
import time
import os
from collections import defaultdict
import glob

# API endpoint and token
BASE_URL = "https://charts-spotify-com-service.spotify.com/auth/v0/charts/regional-il-weekly/"
TOKEN = "BQC8xOmTOrgCRp3ETKXwBaeLfJKdEjg0yI7bBm_r8iwGvYKbhnm3l1TZWFJL11oI5FJ_ZqyRRvMFvdE8bQ-7ekEI-Y686NF6VRi1Evqjzv2YWubK5diZVquu_TEBO0O5-AFzVZ8u34Yb7tI11_gn_Duf7hkiIUqfN1mmXYEu3a5hYx4aDWVLFseQ-CjlCa-ReRrmdsOK"

def get_chart_data(date):
    url = BASE_URL + date.strftime("%Y-%m-%d")
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {date.strftime('%Y-%m-%d')}: {response.status_code} {response.reason}")
        return None

def save_chart_data(data, date):
    if not os.path.exists('chart_data'):
        os.makedirs('chart_data')
    
    filename = f"chart_data/spotify_chart_{date.strftime('%Y-%m-%d')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved data for {date.strftime('%Y-%m-%d')}")

def fetch_all_charts():
    start_date = datetime(2023, 7, 6)  # First Thursday of July 2023
    end_date = datetime(2024, 8, 29)   # Last Thursday of August 2024
    current_date = start_date

    while current_date <= end_date:
        print(f"Fetching data for {current_date.strftime('%Y-%m-%d')}")
        chart_data = get_chart_data(current_date)
        
        if chart_data:
            save_chart_data(chart_data, current_date)
        
        current_date += timedelta(days=7)  # Move to next Thursday
        time.sleep(1)  # Add a delay to avoid overwhelming the API

def process_chart_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Unable to parse JSON in file {file_path}")
            return None, []

    chart_date = data.get('displayChart', {}).get('date')
    if not chart_date:
        chart_date = os.path.basename(file_path).split('_')[2].split('.')[0]

    songs = []

    entries = data.get('entries', [])
    if not entries:
        print(f"Warning: No entries found in {file_path}")
        return chart_date, []

    for entry in entries:
        track_metadata = entry.get('trackMetadata', {})
        chart_entry_data = entry.get('chartEntryData', {})

        song_name = track_metadata.get('trackName', '')
        artists = [artist.get('name', '') for artist in track_metadata.get('artists', [])]
        current_rank = chart_entry_data.get('currentRank', 0)
        if song_name and artists:
            songs.append({
                'song_name': song_name,
                'artists': artists,
                'current_rank': current_rank
            })
        else:
            print(f"Warning: Incomplete data for a song in {file_path}")

    return chart_date, songs

def process_all_chart_files():
    all_chart_data = defaultdict(list)
    
    for file_path in glob.glob('chart_data/spotify_chart_*.json'):
        chart_date, songs = process_chart_file(file_path)
        if chart_date:
            all_chart_data[chart_date].extend(songs)
    
    return dict(all_chart_data)

def main():
    processed_data = process_all_chart_files()

    # Print the result
    print(json.dumps(processed_data, indent=2, ensure_ascii=False))

    # Save the result to a file
    with open('processed_all_chart_data.json', 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)

    print("Processing complete. Results saved to 'processed_all_chart_data.json'")

if __name__ == "__main__":
    main()