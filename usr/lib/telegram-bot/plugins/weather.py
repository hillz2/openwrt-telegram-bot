#!/usr/bin/env python3

import requests
import re
from datetime import datetime
from collections import defaultdict

# Define the URL to fetch data from
urls = [
    'https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=33.09.20.2003',
    'https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=33.09.04.2019'
]

# Mapping weather descriptions to emojis
WEATHER_EMOJIS = {
    "Hujan Ringan": "🌧",
    "Hujan Sedang": "☔️",
    "Hujan Lebat": "💦",
    "Hujan Petir": "⚡"
}

# Function to fetch and process the weather data
def fetch_weather_data(url):
    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON
            weather_data = response.json()

            # Extract location details
            lokasi = weather_data.get("lokasi", {})
            location_name = lokasi.get('desa', 'N/A')
            city_name = lokasi.get('kotkab', 'N/A')

            # Extract weather data
            data = weather_data.get("data", [])
            weather_by_date = defaultdict(list)

            # Process each weather item
            for item in data:
                cuaca = item.get("cuaca", [])

                for period in cuaca:
                    for forecast in period:
                        weather_desc = forecast.get('weather_desc', 'N/A')
                        temperature = forecast.get('t', 'N/A')
                        local_datetime = forecast.get('local_datetime', 'N/A')

                        # Filter for weather descriptions matching "Hujan.*" using regex
                        if re.match(r'Hujan.*', weather_desc):
                            # Parse and format the datetime
                            try:
                                datetime_obj = datetime.strptime(local_datetime, "%Y-%m-%d %H:%M:%S")
                                formatted_date = datetime_obj.strftime("%d-%m-%Y")
                                formatted_time = datetime_obj.strftime("%H:%M")
                            except ValueError:
                                formatted_date = local_datetime
                                formatted_time = ""

                            # Group weather data by date
                            emoji = WEATHER_EMOJIS.get(weather_desc, "🌧️")
                            weather_by_date[formatted_date].append(f"{emoji} {weather_desc}, {temperature}°C at {formatted_time}")

            # Print location and city details
            print(f"### {location_name}, {city_name}")
            for date, weather_list in sorted(weather_by_date.items()):
                print(f"- **{date}**")
                for weather in weather_list:
                    print(f"  - {weather}")
            print()

        else:
            print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to fetch and display the weather data
for url in urls:
    fetch_weather_data(url)
