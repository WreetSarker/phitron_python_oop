import csv
from Airport import Airport
import math

class AllAirport:
    def __init__(self):
        self.airports = None
        self.load_airport_data('./data/airport.csv')

    def load_airport_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}

        # get currency names
        with open('./data/currencyrates.csv', 'r') as file:
            lines = csv.reader(file)

            for line in lines:
                currency_rates[line[1]] = line[2]
        file.close()

        # get country currency
        with open('./data/countrycurrency.csv', 'r') as file:
            lines = csv.reader(file)

            for line in lines:
                country_currency[line[0]] = line[1]

        file.close()

        # create airports
        with open(file_path, 'r', encoding="utf8") as file:
            lines = csv.reader(file)

            try:
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport(line[4], line[1], line[2], line[3], line[6], line[7], rate)

            except KeyError as e:
                # print(e)
                pass

        self.airports = airports

        # for airport in airports.items():
        #     print(airport)



    def get_distance_between_two_airports(self, lat1, lon1, lat2, lon2):
        radius = 6371
        lat_diff = math.radians(lat1 - lat2)
        lon_diff = math.radians(lon1 - lon2)

        arc = (math.sin(lat_diff / 2) * math.sin(lat_diff / 2) +
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
        math.sin(lon_diff / 2) * math.sin(lon_diff / 2))
        c = 2 * math.atan2(math.sqrt(arc), math.sqrt(1 - arc))
        distance = radius * c

        return distance


    def distance_between_two_airports(self, airport1_code, airport2_code):
        airport1 = self.airports[airport1_code]
        airport2 = self.airports[airport2_code]

        distance = self.get_distance_between_two_airports(airport1.lat, airport1.long, airport2.lat, airport2.long)

        return distance

    def ticket_price(self, start, end):
        distance = self.distance_between_two_airports(start, end)
        airport1 = self.airports[start]
        fare = distance * airport1.rate
        return fare

world_tour = AllAirport()
fare = world_tour.ticket_price('DAC', 'PRA')
print(f'Ticket fare: {fare}')