import requests, json, time  #requests → API calls (internet request)
from pathlib import Path #json → Read & write JSON data
from config import API_KEY, BASE_URL #time → Used to check cache expiry
class WeatherAPI: #Defines a class named WeatherAPI Groups all weather related functions
    def __init__(self): #Runs automatically when class object is created
        self.cache_dir = Path("data/cache") #Sets cache folder path Data will be stored here
        self.cache_dir.mkdir(parents=True, exist_ok=True) #Creates folder if not exists No error if already exists
        self.cache_duration = 600 #Cache validity = 600 seconds (10 minutes)

    def _cache_file(self, key): #Private helper function  means internal use
        return self.cache_dir / f"{key}.json" #Creates full path like:

    def _get_cache(self, key): #
        file = self._cache_file(key)
        if file.exists():
            if time.time() - file.stat().st_mtime < self.cache_duration:
                with open(file) as f:
                    data = json.load(f)
                    data["_cached"] = True
                    return data
        return None

    def _save_cache(self, key, data):
        file = self._cache_file(key)
        with open(file, "w") as f:
            json.dump(data, f, indent=2)

    def _request(self, endpoint, params):
        params["appid"] = API_KEY
        params["units"] = "metric"
        r = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
        if r.status_code == 200:
            return r.json()
        return None

    def get_current_weather(self, city):
        key = f"current_{city.lower()}"
        cached = self._get_cache(key)
        if cached:
            return cached

        data = self._request("weather", {"q": city})
        if data:
            data["_cached"] = False
            self._save_cache(key, data)
        return data

    def get_forecast(self, city):
        return self._request("forecast", {"q": city})