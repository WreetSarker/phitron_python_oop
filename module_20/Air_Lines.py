import csv
from Aircraft import Aircraft
class AirLines:
    def __init__(self):
        self.aircrafts = None
        self.load_aircrafts_data('./data/aircraft.csv')

    def load_aircrafts_data(self, csv_file):
        aircrafts = {}
        with open(csv_file, 'r') as file:
            lines = csv.reader(file)
            next(lines)

            for line in lines:
                aircrafts[line[0]] = Aircraft(line[3], line[0], line[1], line[4])

        file.close()
        self.aircrafts = aircrafts

        # for aircraft in aircrafts.items():
        #     print(aircraft)

    def get_aircraft(self, code):
        return self.aircrafts[code]

AirLines()