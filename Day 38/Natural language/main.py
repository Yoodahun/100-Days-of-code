import requests

APP_ID = ""
APP_KEY = ""

WEIGHT_KG = 79.5
HEIGHT_CM = 171.1
AGE = 29
GENDER = "male"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "Content-Type": "application/json"
}

response = requests.post(
    url=EXERCISE_ENDPOINT,
    json=exercise_params,
    headers=headers
)

response.raise_for_status()
print(response.json())