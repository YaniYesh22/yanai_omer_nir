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
AWS_ENDPOINT_URL = 'http://sqs:9324'
AWS_DEFAULT_REGION = 'us-west-1'
sqs = boto3.client('sqs', endpoint_url=AWS_ENDPOINT_URL, region_name=AWS_DEFAULT_REGION)
queue_name = "data-raw-q"
queue_url = None


def create_queue():
    global queue_url
    try:
        response = sqs.get_queue_url(QueueName=queue_name)
        queue_url = response['QueueUrl']
        print(f"Queue URL: {queue_url}")
    except sqs.exceptions.QueueDoesNotExist:
        response = sqs.create_queue(
            QueueName=queue_name,
            Attributes={
                'DelaySeconds': '0',
                'MessageRetentionPeriod': '86400'  # 1 day
            }
        )
        queue_url = response['QueueUrl']
        print(f"Created queue URL: {queue_url}")
    except Exception as e:
        print(f"Error creating queue: {e}")

app = FastAPI()

###############################################################
# API endpoint and token
BASE_URL = "https://charts-spotify-com-service.spotify.com/auth/v0/charts/regional-us-weekly/"
TOKEN = "BQDBCc8Bd5esEzHQhc0DdQ_WtiOj6P9_wigSP_Nmo634ClMs9RD68Cg4zWakgmjng5DbSypOx8hCmhHjgtHExCraMI-Zzx5sUpFQo8J7sv8N7TYwShGIN9fgVpFUvAQjVieTwa9NLE_XrpyUxMWkooI7gtYQ50s4-ijr-8bEnPC6L3as1spCS4Fu-ppZM0yJywdFUrDu"


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

# Send each chart's data to SQS queue
def send_chart_to_sqs(chart_date, chart_summary):
    try:
        message_body = json.dumps({chart_date: chart_summary})
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        print(f"Sent chart data for {chart_date} to SQS. Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"Error sending chart data for {chart_date} to SQS: {e}")

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
            send_chart_to_sqs(chart_date, summary_list)


@app.post("/scrape")
async def scrape():
    if not queue_url:
        create_queue()
    if queue_url and sqs:
        process_all_charts_and_send_to_sqs()
        return JSONResponse(content={"message": "Data fetched and sent to SQS."})
    else:
        return JSONResponse(content={"error": "Failed to send data to SQS."}, status_code=500)
    
