import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.GOOGLE_SHEET_KEY = ""
        self.GOOGLE_SHEET_API_ENDPOINT = "https://api.sheety.co/9f9b62b3fef9c5050eef57ceb4e58bda/copyOfFlightDeals/prices"
        self.google_sheet_header = {
            "Authorization": f"Bearer {self.GOOGLE_SHEET_KEY}"
        }
        self.body = {}

    def updateFlightData(self, data):
        self.body["price"] = data

        response = requests.put(
            url=f"{self.GOOGLE_SHEET_API_ENDPOINT}/{data['id']}",
            headers=self.google_sheet_header,
            json=self.body
        )
        response.raise_for_status()
