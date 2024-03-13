from flight_search import FlightSearch
from datetime import datetime, timedelta


class FlightData:

    def __init__(self, user_data):
        # User data is a json obejcts
        flightSearch = FlightSearch(user_data)
        self.data = flightSearch.search_flights()

    def find_best_fly(self):
        flights = []

        for flight in self.data:
            if flight is not None and flight["has_airport_change"] is False:
                dep_city = flight["cityFrom"]
                dest_city = flight["cityTo"]

                if len(flight["route"]) > 2:
                    stepover_city = flight["route"][1]["cityFrom"]
                    stepover_city_IATA = flight["route"][1]["flyFrom"]
                else:
                    stepover_city = None
                    stepover_city_IATA = None

                dep_date = flight["local_departure"].split("T")[0]
                days = flight["nightsInDest"]
                date = datetime.strptime(dep_date, '%Y-%m-%d')
                back_date = (date + timedelta(days=days)).strftime("%Y-%m-%d")
                print(dep_date)
                print(back_date)

                print(f"Flight from {dep_city} to {dest_city} changed")

                dict = {
                    "lowest_price": flight["price"],
                    "dep_IATA": flight["flyFrom"],
                    "dest_IATA": flight["flyTo"],
                    "dep_city": flight["cityFrom"],
                    "dest_city": flight["cityTo"],
                    "dep_date": dep_date,
                    "back_date": back_date,
                    "stepover_city": stepover_city,
                    "stepover_IATA": stepover_city_IATA
                }

                flights.append(dict)
            else:
                flights.append(None)

        # print(flights)
        return flights
