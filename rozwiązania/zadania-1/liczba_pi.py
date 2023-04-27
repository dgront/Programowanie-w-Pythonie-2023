import random

N = 10000
suma_trafien = 0
for i in range(N):
    x = random.random()
    y = random.random()
    if x * x + y * y < 1:
        suma_trafien += 1
print("pi = ", 4 * suma_trafien / N)