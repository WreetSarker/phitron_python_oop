import hashlib
from brta import BRTA

license_authority = BRTA()
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()

        with open('users.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()
        print(self.name, ' user created')

    @staticmethod
    def logged_in(email, password):
        stored_password = ''
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(' ')[1]
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        # print(stored_password == hashed_password)
        if hashed_password == stored_password:
            print('Valid user')
            return True
        else:
            print('Invalid user')
            return False


class Rider(User):
    def __init__(self, name, email, password, location, balance):
        super().__init__(name, email, password)
        self.location = location
        self.balance = balance


    def set_location(self, location):
        self.location = location

    def get_location(self, location):
        return self.location

    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0

    def take_driving_test(self):
        result = license_authority.driving_test(self.email)
        if result == False:
            pass
        else:
            self.license = result
            self.valid_driver = True



    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination


rahim =  User('Rahim', 'rahim@gmail.com', '2121212')
User.logged_in('rahim@gmail.com', '2144141')
driver = Driver('Wreet Sarker', 'w@gmail.com', '5412', 54, 5242)
print(driver.valid_driver)
license_authority.validate_license(driver.email, driver.license)
driver.take_driving_test()
license_authority.validate_license(driver.email, driver.license)
print(driver.valid_driver)