import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

def fetch_weather(city):
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feel_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        weather_report = f"Weather in {city}, {country}:\n"
        weather_report += "--------------\n"
        weather_report += f"Temperature: {temp}°C (feels like: {feel_like}°C)\n"
        weather_report += f"Condition: {condition}\n"
        weather_report += f"Humidity: {humidity}%\n"
        weather_report += f"Wind speed: {wind_speed} m/s \n"
        
        return weather_report
    except:
        return "Error, please enter a valid city name"