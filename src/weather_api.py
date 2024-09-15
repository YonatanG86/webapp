# weather_api.py
import requests

# Replace this with your actual Visual Crossing API key
API_KEY = 'NV3BTXXZYDFFTJG4HQJB5XG66'


def get_weather_forecast(location, days=7):
    """Fetches the weather forecast for a given location."""
    # Visual Crossing API URL
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={API_KEY}&include=days&contentType=json&forecastDays={days}"
    response = requests.get(url)
    response.raise_for_status()

    return response.json()

def get_icon_url(icon_key):
    icon_base_url = "https://youriconserver.com/icons/"
    return f"/static/icons/{icon_key}.png"