import requests
from flask import Flask, render_template, request, jsonify, flash
from src.weather_day import WeatherDay
from src.weather_api import get_weather_forecast, get_icon_url

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = []
    location_name = None

    if request.method == 'POST':
        location = request.form.get('location')
        try:
            data = get_weather_forecast(location)
            location_name = f"{data['resolvedAddress']}"

            for day in data['days'][:7]:
                weather_day = WeatherDay(
                    date=day['datetime'],
                    max_temp=day['tempmax'],
                    min_temp=day['tempmin'],
                    condition=day['icon'],
                    condition_icon=get_icon_url(day['icon']),
                    humidity=day['humidity']
                )
                weather_data.append(weather_day)

        except requests.exceptions.HTTPError as http_err:
            flash(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            flash(f"Request error occurred: {req_err}")
        except KeyError as key_err:
            flash(f"Error parsing weather data: missing key {key_err}")
        except Exception as e:
            flash(f"An unexpected error occurred: {e}")

    return render_template('index.html', weather_data=weather_data, location_name=location_name)

if __name__ == '__main__':
    app.run(debug=True)
