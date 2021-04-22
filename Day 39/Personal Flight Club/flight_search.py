import requests

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

    def get_flight_data(self):
        body_params = {
            "fly_from":"",
            "date_from":"01/04/2021",
            "date_to":"05/04/2021",
            "return_from":"",
            "return_to":"",
            "flight_type":"round",
            "curr":"GBP"
        }