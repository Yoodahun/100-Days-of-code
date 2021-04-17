import requests
from datetime import datetime

APP_ID = ""
APP_KEY = ""
EXCEL_TOKEN = ""

WEIGHT_KG = 79.5
HEIGHT_CM = 171.1
AGE = 29
GENDER = "male"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
ADD_EXECEL_SHEET_ROW = ""
exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}
excel_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {EXCEL_TOKEN}"
}

exercise_response = requests.post(
    url=EXERCISE_ENDPOINT,
    json=exercise_params,
    headers=exercise_headers
)

exercise_response.raise_for_status()
print(exercise_response.json())
exercise_result = exercise_response.json()

for exercise in exercise_result["exercises"]:

    add_row_params = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.now().time().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }

    print(add_row_params)

    excel_response = requests.post(
        url=ADD_EXECEL_SHEET_ROW,
        json=add_row_params,
        headers=excel_headers

    )
    excel_response.raise_for_status()
