import requests
from datetime import datetime
from datetime import timedelta
from flight_data import FlightData

FLIGHT_SEARCH_API_KEY = ""
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"
GET_LOCATION_QUERY_FLIGHT_SEARCH_ENDPOINT = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"
GET_FLIGHT_SEARCH_ENDPOINT = f"{FLIGHT_SEARCH_ENDPOINT}/v2/search"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.headers = {}
        pass

    def get_headers(self):
        self.headers = {
            "apikey": FLIGHT_SEARCH_API_KEY
        }
        return self.headers

    def get_iataCode(self, cityName):
        body_params = {
            "term": cityName,
            "location_types": "city"
        }

        response = requests.get(
            url=GET_LOCATION_QUERY_FLIGHT_SEARCH_ENDPOINT,
            params=body_params,
            headers=self.get_headers()
        )
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_flight_data(self, origin_city_code, data):
        tomorrow = datetime.today() + timedelta(days=1)
        six_month_later = datetime.today()+ + timedelta(days=(6*30))

        body_params = {
            "fly_to" : data["iataCode"],
            "fly_from":origin_city_code,
            "date_from":tomorrow.strftime("%d/%m/%Y"),
            "date_to":six_month_later.strftime("%d/%m/%Y"),
            "flight_type":"round",
            "one_for_city":1,
            "max_stopovers":0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr":"GBP"
        }

        # print(body_params)

        response = requests.get(
            url=GET_FLIGHT_SEARCH_ENDPOINT,
            params=body_params,
            headers=self.get_headers()
        )

        try:
            flight_response_data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {data['iataCode']}")
            return None

        flight_data = FlightData(
            price=flight_response_data["price"],
            origin_city=flight_response_data["route"][0]["cityFrom"],
            origin_airport=flight_response_data["route"][0]["flyFrom"],
            destination_city=flight_response_data["route"][0]["cityTo"],
            destination_airport=flight_response_data["route"][0]["flyTo"],
            out_date=flight_response_data["route"][0]["local_departure"].split("T")[0],
            return_date=flight_response_data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.arrive_city}: £{flight_data.price}")

        return flight_data