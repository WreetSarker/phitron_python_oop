# class Bus:

#     def __init__(self, name):
#         self._name = name


   
#     @property
#     def get_name(self):
#         return self._name
    
#     @get_name.setter
#     def get_name(self, name):
#         self._name = name


# bus =  Bus("Hanif")
# bus.get_name = "Ena"
# print(bus.get_name)
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} is eating')
    def name(self):
        pass
    @abstractmethod
    def move(self):
        pass



class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print("Monkey is moving")
    
monkey = Monkey("monkey")
monkey.eat()
animal = Animal("dog")

print(monkey == animal)