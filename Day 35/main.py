import os
import requests
import json


# Open Weather API
api_key = os.environ.get("OW_API_KEY")
print(api_key)
lat = 28.574
lng = -81.746


def get_weather():
    req = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lng}&units=imperial&exclude=minutely&appid={api_key}")
    parse = req.json()
    Json_read = json.dumps(parse)

    # Hourly Temps
    hourly_temps = [temp["temp"] for temp in parse["hourly"]]

    # Rain Forecast
    forecast_find = [weather_info["main"] for start in parse["hourly"] for weather_info in start["weather"]]

    # Check rain forecast for rain
    iteration = 0
    for x in forecast_find:
        if x == "Rain":
            print(f"It will rain in {iteration + 1} hours!")
        iteration += 1

    with open("current_weather.txt", 'w') as file:
        json.dump(parse, file)


def iss_overhead():
    iss_request = requests.get("http://api.open-notify.org/iss-now.json")
    iss = iss_request.json()

    iss_lat = float(iss["iss_position"]["latitude"])
    iss_lng = float(iss["iss_position"]["longitude"])

    if iss_lat < 0:
        iss_lat = iss_lat * -1
    if iss_lng < 0:
        iss_lng = iss_lng * -1

    lat_calc = iss_lat / lat
    lng_calc = iss_lng / (lng * -1)

    if .50 > lat_calc < 1.50 and .50 > lng_calc < 1.50:
        print("within range")
        print(iss["iss_position"])
        return True
    else:
        print(lat_calc)
        print(lng_calc)
        print("Not within range")
        return False


# if iss_overhead():
#     print("Hip hip hooray")
# else:
#     print("Nope")

get_weather()
