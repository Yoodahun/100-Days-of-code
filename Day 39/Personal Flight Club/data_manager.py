import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.GOOGLE_SHEET_KEY = ""
        self.GOOGLE_PRICE_SHEET_API_ENDPOINT = "https://api.sheety.co/9f9b62b3fef9c5050eef57ceb4e58bda/copyOfFlightDeals/prices"
        self.GOOGLE_USER_SHEET_API_ENDPOINT = "https://api.sheety.co/9f9b62b3fef9c5050eef57ceb4e58bda/copyOfFlightDeals/users"
        self.google_sheet_header = {
            "Authorization": f"Bearer {self.GOOGLE_SHEET_KEY}"
        }
        self.body = {}

    def update_excel_flight_data(self, data):
        self.body["price"] = data

        response = requests.put(
            url=f"{self.GOOGLE_PRICE_SHEET_API_ENDPOINT}/{data['id']}",
            headers=self.google_sheet_header,
            json=self.body
        )
        response.raise_for_status()

    def add_excel_user_data(self, first_name, last_name, email):

        # response = requests.get(
        #     url=self.GOOGLE_USER_SHEET_API_ENDPOINT,
        #     headers=self.google_sheet_header
        # )

        body = {}
        body["user"] = {}
        print(body)

        body["user"]["firstName"] = first_name
        body["user"]["lastName"] = last_name
        body["user"]["email"] = email

        response = requests.post(
            url=self.GOOGLE_USER_SHEET_API_ENDPOINT,
            headers=self.google_sheet_header,
            json=body
        )
        response.raise_for_status()
        print(response.json())
        print("You're in the club!")
