import random

class BRTA:
    def __init__(self):
        self.__licenses = {}


    def driving_test(self, email):
        score = random.randint(0, 100)
        if score > 33:
            print(f"Congrats! ", score)
            license_number = random.randint(5000, 9999)
            self.__licenses[email] = license_number
            return license_number
        else:
            print("Sorry! You failed ", score)
            return False


    def validate_license(self, email, license):
        if self.__licenses.get(email) is not None:
            return self.__licenses[email] == license
        return False