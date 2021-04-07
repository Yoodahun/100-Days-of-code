import requests

END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
lat = 33.590355
lon = 130.401718

weather_params = {
    "lat":lat,
    "lon":lon,
    "appid":API_KEY,
    "exclude": "current,minutely,daily"
}

# response = requests.get(f"{END_POINT}?lat={lat}&lon={lon}&exclude=&appid={API_KEY}")
response = requests.get(END_POINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]

for hour in weather_data:
    print(hour)
    if hour["weather"][0]["id"] < 700:
        print("Bring an Umbrella")



# for hour in range(0,12):
#     print(hour)
#     if weather_data[hour]["weather"][0]["id"] < 700:
#         print("Bring an Umbrella")

# print(weather_data["hourly"])
# hourly[0][weather][0][id]