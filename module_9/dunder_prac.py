class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


person1 = Person("Wreet", 25)
person2 = Person("Wreet", 25)

print(person1 + person2)
print(person1 == person2)