import math
import time

def timer(func):
    def inner():
        print("Time start")
        func()
        print("Time end")
    return inner

@timer
def printHello():
    print("Hello")

printHello()


def factorial(n):
    start = time.time()
    fac = math.factorial(n)
    end = time.time()

    print(f"Factorial of {n} is {fac} and time taken = {end-start}")


factorial(200)