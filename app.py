from flask import Flask, request, render_template
import requests
import logging
from datetime import datetime, timedelta

logging.basicConfig(filename='logs/error.log', level=logging.DEBUG)

app = Flask(__name__)

def get_next_5_days():
    today = datetime.now()
    next_5_days = [today + timedelta(days=i) for i in range(5)]
    return [day.strftime("%Y-%m-%d") for day in next_5_days]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    api_key = 'a61406e23e9f080057d7f261289d26ae'
    user_input = request.form.get('city')

    try:
        weather_response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}"
        )
        if weather_response.status_code != 200:
            raise ValueError(f"Weather API call failed with status code {weather_response.status_code}")

        weather_data = weather_response.json()
        weather_main = weather_data['weather'][0]['main']
        icon_filename = f"{weather_main}.svg"

        forecast_response = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={user_input}&units=metric&appid={api_key}"
        )
        if forecast_response.status_code != 200:
            raise ValueError(f"Forecast API call failed with status code {forecast_response.status_code}")

        forecast_data = forecast_response.json()
        forecast_result = forecast_data['list']

        return render_template(
            'result.html',
            user_input=user_input,
            weather_data=weather_data,
            forecast_result=forecast_result,
            icon_filename=icon_filename
        )
    except Exception as e:
        logging.error(f"Error in get_weather: {e}", exc_info=True)
        return render_template('error.html', error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
