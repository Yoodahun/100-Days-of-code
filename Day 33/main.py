import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(data)
# print(iss_position)

# https://api.sunrise-sunset.org/json


parameter = {
    "lat" : 33.590355,
    "lng" : 130.401718,
    "formatted": 0

}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)

time_now = dt.datetime.now()


print(time_now.hour)