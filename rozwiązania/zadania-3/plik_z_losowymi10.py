import random

with open("nazwa.txt","w") as plik:
    for i in range(10):
        print(random.randint(0,10), file=plik)
# plik zamykany jest automatycznie po wyjściu z bloku "with"
