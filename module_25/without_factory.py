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


b1 = Bike("Wreet", 5)
c1 = Car("Rahim", 12)
print(b1.get_fare(20))
print(c1.get_fare(12))