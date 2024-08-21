import requests
import json

def scrape_spotify_charts():
    url = "https://charts-spotify-com-service.spotify.com/public/v0/charts"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        results = []
        
        # Navigate to the correct part of the JSON structure
        chart_entries = data['chartEntryViewResponses'][0]['entries']
        
        for entry in chart_entries:
            track_metadata = entry['trackMetadata']
            song_name = track_metadata['trackName']
            artists = [artist['name'] for artist in track_metadata['artists']]
            
            results.append({
                'song_name': song_name,
                'artists': artists
            })
        
        
        return results
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching the data: {e}")
        return []
    except (KeyError, IndexError) as e:
        print(f"Error parsing the JSON data: {e}")
        return []
    
def create_json_output(results):
    return json.dumps(results, indent=2)

# Scrape the data
scraped_data = scrape_spotify_charts()

# Create JSON output
json_output = create_json_output(scraped_data)

# Print the JSON
print(json_output)

# Optionally, save the JSON to a file
with open('spotify_charts.json', 'w') as f:
    f.write(json_output)