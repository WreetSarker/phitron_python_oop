from abc import ABC, abstractmethod

class Vehicle(ABC):
    speeds = {
        'car':30,
        'bike':50,
        'cng':15
    }

    def __init__(self, vehicle_type, license_plate, rate, driver):
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.license_plate = license_plate
        self.speed = speeds[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        print(self.vehicle_type, " started")
        

    def trip_finished(self):
        print(self.vehicle_type, " finished trip")