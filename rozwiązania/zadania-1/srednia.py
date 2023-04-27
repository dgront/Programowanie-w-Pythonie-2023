import random

N = 10000
suma = 0
for i in range(N):
    suma += random.random()
print("srednia = ", suma / N)