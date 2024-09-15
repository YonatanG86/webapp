# weather_api.py
import requests

API_KEY = 'b7ec68d1817c4fc19db183248241209'

def get_weather_forecast(location, days=7):
    """Fetches the weather forecast for a given location."""
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days={days}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_autocomplete_suggestions(query):
    """Fetches autocomplete suggestions for a given query."""
    url = f"http://api.weatherapi.com/v1/search.json?key={API_KEY}&q={query}"
    response = requests.get(url)
    response.raise_for_status()
    suggestions = response.json()

    # Use a dictionary to remove duplicates based on both name and country
    unique_suggestions = {}
    for suggestion in suggestions:
        key = f"{suggestion['name']}, {suggestion['country']}"
        if key not in unique_suggestions:
            unique_suggestions[key] = suggestion

    # Convert the dictionary back to a list
    return list(unique_suggestions.values())
