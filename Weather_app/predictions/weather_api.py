import requests
from dotenv import load_dotenv
import os
from django.conf import settings

load_dotenv()

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": os.getenv("API_KEY"),# settings.OPENWEATHER_API_KEY 
        "units": "metric"
    }
    
    r = requests.get(url, params=params)
    data = r.json()
    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "pressure": data["main"]["pressure"]
    }
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}