from datetime import datetime

def time_fmt(ts):
    return datetime.fromtimestamp(ts).strftime("%H:%M")

def parse_current(d):
    return {
        "city": d["name"],
        "country": d["sys"]["country"],
        "temp": d["main"]["temp"],
        "feels": d["main"]["feels_like"],
        "condition": d["weather"][0]["description"],
        "humidity": d["main"]["humidity"],
        "wind": round(d["wind"]["speed"] * 3.6),
        "pressure": d["main"]["pressure"],
        "visibility": int(d.get("visibility", 0) / 1000),
        "sunrise": time_fmt(d["sys"]["sunrise"]),
        "sunset": time_fmt(d["sys"]["sunset"]),
        "updated": datetime.fromtimestamp(d["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
        "cached": d.get("_cached", False)
    }

def parse_forecast(data):
    days = {}
    for i in data["list"]:
        date = i["dt_txt"].split()[0]
        if date not in days:
            days[date] = i
    return list(days.values())[:5]