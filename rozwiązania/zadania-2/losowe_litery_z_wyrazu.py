import random

napis = "konstantynopolitańczykowianeczka"
N = len(napis)
for i in range(10):
    index = random.randint(0,N-1)
    print(napis[index], end=" ")