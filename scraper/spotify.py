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
TOKEN = "BQADJfegDKvieQDts_rjVBt5CM5fQ4INn1o_UqGci7sMX7EK3WRdQPuSvr_w4XLXONKhCe708dPRzmLwhHoNJBEpEzijahy600uM_gI5AUuZNJrb6a9ilc8uQ_TRkpkIvCgNgTR7lUvncLjuHNc7LmExYruDaVi06zneA--po8tSACQpZfJ_myDNub-viyQtDluExdzg"

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

def send_to_sqs(data):
    if queue_url and sqs:
        compressed_message = compress_message(data)
        if data:
        # if len(compressed_message) <= 256 * 1024:  # Ensure the message doesn't exceed 256 KB
            response = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=data
            )
            print(f"Sent message to SQS: {response['MessageId']}")
        else:
            print("Error: Message is too large even after compression.")
    else:
        print("Error: Queue URL not available or SQS client not initialized.")

def fetch_all_charts():
    start_date = datetime(2024, 6, 6)  # First Thursday of July 2024
    end_date = datetime(2024, 8, 22)   # Last Thursday of August 2024
    current_date = start_date

    while current_date <= end_date:
        print(f"Fetching data for {current_date.strftime('%Y-%m-%d')}")
        chart_data = get_chart_data(current_date)
        
        if chart_data:
            save_chart_data(chart_data, current_date)
            # Send the data to SQS
            send_to_sqs(json.dumps(chart_data, ensure_ascii=False))
        
        current_date += timedelta(days=7)  # Move to next Thursday
        time.sleep(1)  # Add a delay to avoid overwhelming the API

def compress_message(message):
    compressed = gzip.compress(message.encode('utf-8'))
    return base64.b64encode(compressed).decode('utf-8')

@app.post("/scrape")
async def scrape():
    if not queue_url:
        create_queue()
    if queue_url and sqs:
        fetch_all_charts()
        return JSONResponse(content={"message": "Data fetched and sent to SQS."})
    else:
        return JSONResponse(content={"error": "Failed to send data to SQS."}, status_code=500)
    
@app.post("/send")
async def scrape():
    if not queue_url:
        create_queue()
    if queue_url and sqs:
        send_to_sqs(json.dumps('send Data', ensure_ascii=False))
        return JSONResponse(content={"message": "Data fetched and sent to SQS."})
    else:
        return JSONResponse(content={"error": "Failed to send data to SQS."}, status_code=500)
