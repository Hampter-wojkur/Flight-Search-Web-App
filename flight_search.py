import json
import requests
from sheety_data import DataManager
from datetime import datetime
from dateutil.relativedelta import relativedelta


class FlightSearch:
    # Change static departues to dynamic
    # POLAND_IATA = "KRK,KTW"
    flight_url = "https://api.tequila.kiwi.com/v2/search"

    # def __init__(self, date_from, date_to, destinations, departures, max_prices, accept_stopover, currency, max_days_at_dest):
    def __init__(self, data):
        # Data is a json object

        # Date data
        self.date_from = data["date_from"]
        self.date_to = data["date_to"]
        self.max_days = int(data["max_days_at_destination"])
        # Place data
        self.departures = data["departures"]
        self.destinations = data["arrivals"]
        # Price data
        self.max_prices = data["max_flight_prices"]
        self.currency = data["currency"]
        # Rest
        self.accept_stopover = bool(data["accept_stopovers"])

    def search_flights(self):
        # DATE MUST BE IN (dd/mm/yyyy) FORMAT (string)

        # today_date = datetime.now().strftime("%d/%m/%Y")
        # six_month_later = datetime.now() + relativedelta(months=5)
        # print(six_month_later.strftime("%d/%m/%Y"))

        # data_manager_instance = DataManager()
        # destinations, prices = data_manager_instance.get_iatas_and_prices()
        responds = []

        flight_header = {
            "apikey": "LgKc60UiKJFmzRjXid63dTu5xpABqtz7",
            "Content-Type": "application/json",
            "Content-Encoding": "gzip"
        }

        for destination, price in zip(self.destinations, self.max_prices):
            body = {
                "fly_from": self.departures,
                "fly_to": destination,
                "date_from": self.date_from,
                "date_to": self.date_to,
                "curr": self.currency,
                "price_to": price,
                "max_stopovers": 0,
                "nights_in_dst_from": 2,
                "nights_in_dst_to": self.max_days
                }

            respond = requests.get(url=self.flight_url, headers=flight_header, params=body)
            data = respond.json()
            json_respond = json.dumps(respond.json())
            # print(data)
            # print(json_respond)

            if data["_results"] != 0 and data["data"][0]["price"] < price:
                print(data["data"][0])
                responds.append(data["data"][0])
            elif data["_results"] == 0:
                print(f"Nie znaleziono bezpośredniego lotu do {destination}, szukanie z przesiadką")

                if self.accept_stopover is True:

                    body["max_stopovers"] = 2
                    respond2 = requests.get(url=self.flight_url, headers=flight_header, params=body)
                    data2 = respond2.json()

                    # Znaleziono z przesiadką i cena niższa

                    if data2["_results"] != 0 and data2["data"][0]["price"] < price:
                        print(f"Znaleziono lot do {destination} z przesiadką!")
                        print(data2["data"][0])
                        responds.append(data2["data"][0])
                    else:
                        print(f"Nie znaleziono lotu z jedną przesiadką, brak lotów do {destination} lub za wysoka cena.")
                        responds.append(None)

                else:
                    print(f"Brak lotów do {destination} lub za wysoka cena, (opcja z przesiadką nie została wybrana).")

            else:
                print(f"Znaleziono bezpośredni lot do {destination}, ale cena nie była korzystniejsza")
                responds.append(None)

        return responds

# flightSearch = FlightSearch()
# flightSearch.search_flights()
# print(destinations)
# print(prices)
# today_date = datetime.now().strftime("%d/%m/%Y")
# six_month_later = datetime.now() + relativedelta(months=5)
# print(six_month_later.strftime("%d/%m/%Y"))
