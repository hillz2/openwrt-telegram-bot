#!/usr/bin/env python3

import requests
import re
from datetime import datetime

# Define the URL to fetch data from
urls = [ 
    'https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=33.09.20.2003',
    'https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=33.09.04.2019'
]
# Function to fetch and process the weather data
def fetch_weather_data(url):
    try:
        # Send a GET request to the API
        response = requests.get(url, timeout=20)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON
            weather_data = response.json()

            # Extract and format the necessary data
            lokasi = weather_data.get("lokasi", {})
            data = weather_data.get("data", [])

            # Print the location information
            print(f"Location: {lokasi.get('desa', 'N/A')}")
            print(f"City: {lokasi.get('kotkab', 'N/A')}")
            print("-" * 50)

            # Iterate through the weather data and print the required fields
            for item in data:
                lokasi_data = item.get("lokasi", {})
                cuaca = item.get("cuaca", [])

                # Iterate through each hourly forecast
                for period in cuaca:
                    for forecast in period:
                        desa = lokasi_data.get('desa', 'N/A')
                        local_datetime = forecast.get('local_datetime', 'N/A')
                        weather_desc = forecast.get('weather_desc', 'N/A')
                        temperature = forecast.get('t', 'N/A')
                        analysis_date = forecast.get('analysis_date', 'N/A')

                        # Filter weather descriptions that match "Hujan.*" using regex
                        if re.match(r'Hujan.*', weather_desc):
                            try:
                                # Convert the local_datetime to the desired format
                                local_datetime_obj = datetime.strptime(local_datetime, "%Y-%m-%d %H:%M:%S")
                                formatted_local_datetime = local_datetime_obj.strftime("%d-%m-%Y %H:%M:%S")
                            except ValueError:
                                formatted_local_datetime = local_datetime  # In case of invalid datetime format

                            # Print the formatted weather details with a bullet point
                            print(f"• {weather_desc}. Temp: {temperature}°C at {formatted_local_datetime}")

        else:
            print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to fetch and display the weather data
for url in urls:
    fetch_weather_data(url)
    print("-" * 50)
