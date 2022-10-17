import time
from functools import cache


@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)


start = time.time()

for i in range(900):
    print(i, fib(i))

end = time.time()

print(f"Time took: {end-start}")