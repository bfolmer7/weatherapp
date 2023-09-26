from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    api_key = 'a61406e23e9f080057d7f261289d26ae'
    user_input = request.form.get('city')

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}"
    )

    if weather_data.status_code == 404:
        result = "No City Found"
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        country = weather_data.json()['sys']['country']
        feels_like = round(weather_data.json()['main']['feels_like'])

        result = f"The weather in {user_input}, {country} is {weather}\n"
        result += f"The temperature in {user_input}, {country} is {temp}ºC\n"
        result += f"It currently feels like {feels_like}ºC in {user_input}\n"

        if weather == "Clouds":
            result += "☁"
        elif weather == "Clear":
            result += "☀"
        elif weather == "Drizzle":
            result += "🌧"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
