import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

# ORIGIN_CITY_DEPARTURE = "LON"
#
# # This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# # program requirements.
flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
#
# response = requests.get(
#     url=data_manager.GOOGLE_PRICE_SHEET_API_ENDPOINT,
#     headers=data_manager.google_sheet_header
# )
#
# response.raise_for_status()
# sheet_data = response.json()["prices"]
# pprint(response.json()["prices"])
#
# for data in sheet_data:
#
#     if data["iataCode"] == "":
#         data["iataCode"] = flight_search.get_iataCode(data["city"])
#
#     data_manager.update_excel_flight_data(data)
#
# response = requests.get(
#     url=data_manager.GOOGLE_PRICE_SHEET_API_ENDPOINT,
#     headers=data_manager.google_sheet_header
# )
#
# for data in response.json()["prices"]:
#     search_result = flight_search.get_flight_data(
#         ORIGIN_CITY_DEPARTURE,
#         data
#     )
#
#     if search_result is None:
#         continue
#
#     if search_result.price < data["lowestPrice"]:
#         notification_manager.notification(
#             price=search_result.price,
#             origin_city= search_result.departure_city,
#             origin_airport= search_result.departure_airport_code,
#             destination_city= search_result.arrive_city,
#             destination_airport= search_result.arrive_airport_code,
#             out_date=search_result.out_date,
#             return_date=search_result.return_date
#         )
#

print("Welcome to Dahun's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
check_email = input("Type your email again. ")

while email != check_email:
    check_email = input("Not matched. Type your email again. ")

data_manager.add_excel_user_data(first_name, last_name, email)

