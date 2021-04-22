import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
flight_search = FlightSearch()
data_manager = DataManager()


response = requests.get(
    url=data_manager.GOOGLE_SHEET_API_ENDPOINT,
    headers=data_manager.google_sheet_header
)

response.raise_for_status()
sheet_data = response.json()["prices"]
pprint(response.json()["prices"])



for data in sheet_data:

    if data["iataCode"] == "":
        data["iataCode"] = flight_search.get_iataCode(data["city"])

    data_manager.update_excel_flight_data(data)


response = requests.get(
    url=data_manager.GOOGLE_SHEET_API_ENDPOINT,
    headers=data_manager.google_sheet_header
)
pprint(response.json()["prices"])