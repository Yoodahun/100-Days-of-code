class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, stop_overs=0, via_citys=""):
        self.price = price
        self.departure_city = origin_city
        self.departure_airport_code = origin_airport
        self.arrive_city = destination_city
        self.arrive_airport_code = destination_airport
        self.out_date = out_date
        self.return_date =return_date

        self.stop_overs = stop_overs
        self.via_city = via_citys




