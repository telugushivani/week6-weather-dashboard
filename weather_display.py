icons = {
    "rain": "🌧️",
    "cloud": "☁️",
    "clear": "☀️",
    "snow": "❄️",
    "mist": "🌫️"
}

def icon(txt):
    for k in icons:
        if k in txt.lower():
            return icons[k]
    return "⛅"

def display_dashboard(c, forecast):
    print("\nWEATHER DASHBOARD")
    print("="*23)

    print(f"\n📍 Current Location: {c['city']}, {c['country']}")
    print(f"🕐 Last Updated: {c['updated']}")

    print("\nCurrent Weather:")
    print("────────────────")
    print(f"Temperature:   {c['temp']}°C (Feels like: {c['feels']}°C)")
    print(f"Conditions:    {c['condition'].title()} {icon(c['condition'])}")
    print(f"Humidity:      {c['humidity']}%")
    print(f"Wind:          {c['wind']} km/h")
    print(f"Pressure:      {c['pressure']} hPa")
    print(f"Visibility:    {c['visibility']} km")
    print(f"Sunrise:       {c['sunrise']}")
    print(f"Sunset:        {c['sunset']}")

    print("\n5-Day Forecast:")
    print("───────────────")
    for f in forecast:
        d = f["dt_txt"].split()[0]
        desc = f["weather"][0]["description"]
        hi = f["main"]["temp_max"]
        lo = f["main"]["temp_min"]
        hum = f["main"]["humidity"]
        print(f"{d}: {icon(desc)}  {hi}°C / {lo}°C  (Humidity: {hum}%)")

    if c["cached"]:
        print("\nAPI Status: Using cached data (5 minutes old)")
    else:
        print("\nAPI Status: Live data")