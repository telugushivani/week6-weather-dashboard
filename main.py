from weather_api import WeatherAPI
from weather_parser import parse_current, parse_forecast
from weather_display import display_dashboard

api = WeatherAPI()

while True:
    city = input("\nType city name or 'quit': ")

    if city.lower() == "quit":
        break

    cur_raw = api.get_current_weather(city)
    fore_raw = api.get_forecast(city)

    if not cur_raw or not fore_raw:
        print("Failed to fetch data")
        continue

    current = parse_current(cur_raw)
    forecast = parse_forecast(fore_raw)

    display_dashboard(current, forecast)