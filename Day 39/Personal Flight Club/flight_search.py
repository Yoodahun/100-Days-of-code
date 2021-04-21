import requests

FLIGHT_SEARCH_API_KEY = ""
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"
GET_LOCATION_QUERY_FLIGHT_SEARCH_ENDPOINT = f"{FLIGHT_SEARCH_ENDPOINT}/locations/query"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.headers = {}
        pass

    def getHeaders(self):
        self.headers = {
            "apikey": FLIGHT_SEARCH_API_KEY
        }
        return self.headers

    def getIataCode(self, cityName):
        body_params = {
            "term": cityName,
            "location_types": "city"
        }

        response = requests.get(
            url=GET_LOCATION_QUERY_FLIGHT_SEARCH_ENDPOINT,
            params=body_params,
            headers=self.getHeaders()
        )
        response.raise_for_status()
        return response.json()["locations"][0]["code"]
