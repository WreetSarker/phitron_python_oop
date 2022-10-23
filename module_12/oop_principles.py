class Bus:
    owner = "Hanif Enterprise"

    def __init__(self, route, license, driver):
        self.route = route
        self.license = license
        self.driver = driver
        self.trips = []
    
    def start_trip(self, start_time):
        self.trips.append(start_time)


class Driver:
    def __init__(self, name, license):
        pass

bus = Bus("dhaka to sylhet", "DHK123", "Rahim")