import requests
import datetime

USERNAME = "dahun"
TOKEN = ""

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.json())


GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name":"TestGraph",
    "unit":"commit",
    "color": "momiji",
    "type":"int"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=GRAPH_ENDPOINT,
#                          json=graph_params,
#                          headers=headers
#                          )
# print(response.json())

POST_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
post_graph_params = {
    "date":"20210413",
    "quantity":"3"
}

response = requests.post(url=POST_GRAPH_ENDPOINT,
                         json=post_graph_params,
                         headers=headers
                         )
print(response.json())