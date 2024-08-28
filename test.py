import requests
from datetime import datetime, timedelta
import json
import time
import os
from collections import defaultdict
import glob
import boto3
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import gzip
import base64

################################################################



###############################################################
# API endpoint and token
BASE_URL = "https://charts-spotify-com-service.spotify.com/auth/v0/charts/regional-us-weekly/"
TOKEN = "BQDlrfjEgfqYM4Zva8AeLjylX_Q3Z27BDfob8jSrTeU569Pr0qfYD2YF0EBFqFjfkcJV3SfYNXQlzDs0sj9q_gowVc9GTW_JR_6U7A_xnVnzOcFB6cRko3AzOTNdGcLTzrbmfVhzPP1En0RB_3OvoNreC-FMgRlX9B7IiXCJoN1iT2glHfFg0O6xFEYjRZCuMu0067ne"


# Fetch and save chart data
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
    start_date = datetime(2023, 8, 3)
    end_date = datetime(2024, 8, 16)
    current_date = start_date

    while current_date <= end_date:
        print(f"Fetching data for {current_date.strftime('%Y-%m-%d')}")
        chart_data = get_chart_data(current_date)
        
        if chart_data:
            save_chart_data(chart_data, current_date)
        
        current_date += timedelta(days=7)  # Move to next Thursday
        time.sleep(1)  # Add a delay to avoid overwhelming the API


# Combine all chart summaries and send each to the SQS queue
def process_all_charts_and_send_to_sqs():
    fetch_all_charts()
    chart_files_directory = "chart_data"

    for file_name in os.listdir(chart_files_directory):
        file_path = os.path.join(chart_files_directory, file_name)

        with open(file_path, 'r', encoding='utf-8') as f:
            chart_data = json.load(f)
            chart_date = chart_data.get("displayChart", {}).get("date", "unknown_date")

            summary_list = []

            # Only process the top 10 entries
            for entry in chart_data.get("entries", [])[:10]:
                song_name = entry.get("trackMetadata", {}).get("trackName", "Unknown Song")
                current_rank = entry.get("chartEntryData", {}).get("currentRank", "Unknown Rank")
                release_date = entry.get("trackMetadata", {}).get("releaseDate", "Unknown Date")
                artists = [
                    artist.get("name", "Unknown Artist")
                    for artist in entry.get("trackMetadata", {}).get("artists", [])
                ]

                song_summary = {
                    "song_name": song_name,
                    "current_rank": current_rank,
                    "artists": artists,
                    "release_date": release_date
                }
                summary_list.append(song_summary)

            # Send each date's top 10 chart summary to SQS
            print(chart_date, summary_list)

if __name__ == '__main__':
    fetch_all_charts()