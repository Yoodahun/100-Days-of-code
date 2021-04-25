class NotificationManager:

    def __init__(self):
        pass

    def notification(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        print(f"Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date} to {return_date}.")

