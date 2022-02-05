import random

N = 10000
n = 0
for i in range(N):
    x = random.random()
    y = random.random()
    if x * x + y * y < 1:
        n += 1
print("pi = ", 4 * n / N)