import requests
from datetime import datetime

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
    "date":datetime.today().strftime("%Y%m%d"),
    "quantity":"3"
}

# response = requests.post(url=POST_GRAPH_ENDPOINT,
#                          json=post_graph_params,
#                          headers=headers
#                          )

PUT_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/20210414"
put_graph_params = {
    "quantity":"7"
}
# response = requests.put(url=PUT_GRAPH_ENDPOINT,
#                         json=put_graph_params,
#                         headers=headers)

DELETE_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}/20210414"

response = requests.delete(url=DELETE_GRAPH_ENDPOINT,
                           headers=headers)

print(response.json())