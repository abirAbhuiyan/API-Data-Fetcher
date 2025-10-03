import requests
import pandas as pd
from openai import OpenAI

# ===== CONFIG =====
OPENWEATHER_API_KEY = "your_api_key_here"
cities = ["Dhaka", "New York", "London", "Tokyo", "Paris"]

# ===== FETCH WEATHER DATA =====
weather_data = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            weather_data.append({
                "City": city,
                "Temperature (°C)": data["main"]["temp"],
                "Weather": data["weather"][0]["description"].title(),
                "Humidity (%)": data["main"]["humidity"]
            })
        elif response.status_code == 401:
            print(f"Invalid OpenWeatherMap API key. Cannot fetch data for {city}.")
        else:
            print(f"Failed to fetch data for {city}. Status code: {response.status_code}")
            print("Response:", data)
            
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")

# ===== SAVE TO CSV =====
if weather_data:
    df = pd.DataFrame(weather_data)
    df.to_csv("weather_data.csv", index=False)
    print("Weather data saved to weather_data.csv")
    print(df)
else:
    print("No weather data collected. Check your OpenWeatherMap key.")
