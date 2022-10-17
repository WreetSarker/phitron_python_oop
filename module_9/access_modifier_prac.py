class Person:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.__phone = phone

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value


wreet = Person("Wreet", '12345', '0131313')
print(wreet.password)