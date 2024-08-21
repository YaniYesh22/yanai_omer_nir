import requests
from bs4 import BeautifulSoup
import json

def clean_artist_names(artist_string):
    # Normalize common indicators to a single format for splitting
    separators = ['Featuring', 'Feat', 'feat', '&', ',']
    for sep in separators:
        artist_string = artist_string.replace(sep, ",")
    # Split the string and strip whitespace from each name
    return [name.strip() for name in artist_string.split(",") if name.strip()]

def scrape_billboard_chart(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    chart_data = []
    main_container = soup.find('div', class_='chart-results-list')
    entries = main_container.find_all('div', class_='o-chart-results-list-row-container')

    for entry in entries:
        # Extract the rank
        rank = entry.find('li', class_='o-chart-results-list__item').find('span', class_='c-label').get_text(strip=True)

        # Extract song title and artist name
        details = entry.find('li', class_='lrv-u-width-100p')
        if details:
            song_title = details.find('h3').get_text(strip=True) if details.find('h3') else 'Unknown Song'
            artist_name = details.find('span').get_text(strip=True) if details.find('span') else 'Unknown Artist'
            # Clean and split artist names
            artists = clean_artist_names(artist_name)
        else:
            song_title = 'Unknown Song'
            artists = ['Unknown Artist']

        chart_data.append({
            'rank': rank,
            'artists': artists,  # Use plural key 'artists' for clarity
            'song_name': song_title
        })
    
    return chart_data

# URL to scrape
url = 'https://www.billboard.com/charts/tiktok-billboard-top-50/'

# Scrape the data
chart_entries = scrape_billboard_chart(url)

# Write data to a JSON file
with open('tiktok_billboard_data.json', 'w') as json_file:
    json.dump(chart_entries, json_file, indent=4)

print("Data has been written to 'tiktok_billboard_data.json'")
