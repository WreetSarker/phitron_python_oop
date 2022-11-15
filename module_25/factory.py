class Bike:
    def __init__(self, driver, rate):
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return distance*self.rate

class Car:
    def __init__(self, driver, rate):
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return distance*self.rate

class CNG:
    def __init__(self, driver, rate):
        self.rate = rate
        self.driver = driver

    def get_fare(self, distance):
        return distance*self.rate


def Factory(company_name):
    vehicles = {
        'car':Car,
        'bike':Bike,
        'cng':CNG
    }

    return vehicles[company_name]()

c1 = Factory('car')