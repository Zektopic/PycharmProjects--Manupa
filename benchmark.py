import time
import math

def name_original(total):
    for item in range(1, 21):
        total *= item

def name_optimized(total):
    total *= math.factorial(20)

start = time.perf_counter()
for _ in range(100000):
    name_original(1)
end = time.perf_counter()
print(f"Original: {end - start:.6f} seconds")

start = time.perf_counter()
for _ in range(100000):
    name_optimized(1)
end = time.perf_counter()
print(f"Optimized: {end - start:.6f} seconds")
