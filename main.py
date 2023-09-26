import requests

api_key = 'a61406e23e9f080057d7f261289d26ae'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    country = weather_data.json()['sys']['country']
    feels_like = round(weather_data.json()['main']['feels_like'])

    print(f"The weather in {user_input}, {country} is {weather}" )
    print(f"The temperature in {user_input}, {country} is {temp}ºC")
    print(f"It currently feels like {feels_like}ºC in {user_input}")

if weather == "Clouds":
        print("☁")
elif weather == "Clear":
    print("☀")
elif weather == "Drizzle":
    print("🌧")