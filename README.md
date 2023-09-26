# Flask Weather App

A simple web application built with Flask that allows users to check the weather for a specific city.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Key](#api-key)
- [Contributing](#contributing)


## Description

This Flask Weather App provides users with real-time weather information for a city. It utilizes the OpenWeatherMap API to fetch weather data based on user input and displays it in a user-friendly interface.

## Features

- User-friendly web interface.
- Real-time weather data retrieval.
- Displays weather condition, temperature, and more.
- Error handling for invalid city inputs.

## Installation

1. Clone this repository to your local machine:

   ```bash
   https://github.com/bfolmer7/weatherapp.git
  
2. Navigate to the project directory:
  
  cd flask-weather-app

3. Install the required dependencies using pip:
  
  pip install -r requirements.txt

## Usage
Run the Flask application:

1. In your terminal emter: python app.py

2. Open your web browser and visit http://localhost:5000.

3. Enter the name of a city in the input field and click the "Get Weather" button to retrieve weather information.

## API Key
This project uses the OpenWeatherMap API to fetch weather data. To make it work, you need to obtain an API key from OpenWeatherMap and replace the api_key variable in app.py with your API key.

api_key = 'your_api_key_here'


## Contributing

Contributions are welcome! If you have any ideas, enhancements, or bug fixes, please open an issue!



