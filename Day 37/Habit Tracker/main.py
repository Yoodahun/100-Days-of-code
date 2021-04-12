import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": "thisistoken",
    "username": "dahun",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(PIXELA_ENDPOINT, json=user_params)
print(response.json())