import os #module is used to interact with operating system
from dotenv import load_dotenv #Imports load_dotenv() function from python-dotenv package.

load_dotenv() #This loads all key-value pairs from .env file into environment.

API_KEY = os.getenv("OPENWEATHER_API_KEY") #Gets the value of OPENWEATHER_API_KEY from environment.
BASE_URL = "https://api.openweathermap.org/data/2.5" #This is the base URL of OpenWeather API

if not API_KEY: #Checks if API_KEY is empty or missing.
    raise ValueError("API Key missing in .env file") #Stops the program and shows custom error message