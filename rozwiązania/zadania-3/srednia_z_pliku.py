import random

with open("nazwa.txt","w") as plik:
    for i in range(10):
        print(random.random(), file=plik)

suma = 0.0
mianownik = 0.0
with open("nazwa.txt") as plik:
    plik = open("nazwa.txt")
    for linia in plik:
        wyrazy = linia.strip().split()
        for wyraz in wyrazy:
            if wyrazy.isnumeric():
                suma = suma + float(wyrazy[0])
                mianownik = mianownik + 1

print(suma/mianownik)