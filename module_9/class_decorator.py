class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f'{first.lower()}.{last.lower()}@gmail.com'

    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, val):
        self.email = val


user = User("Wreet", "Sarker")
user.email = "abc@gmail.com"
print(user.email)