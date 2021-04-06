import requests

END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
lat = 33.590355
lon = 130.401718

weather_params = {
    "lat":lat,
    "lon":lon,
    "appid":API_KEY
}

# response = requests.get(f"{END_POINT}?lat={lat}&lon={lon}&exclude=&appid={API_KEY}")
response = requests.get(END_POINT, params=weather_params)
print(response.status_code)
print(response.json()["hourly"])