import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

import random
n = random.randint(15, 35)

start_time = time.time()
result = fibonacci(n)
end_time = time.time()

print(f"The {n}th term of the Fibonacci sequence is: {result}")
print(f"Time taken: {end_time - start_time} seconds")
