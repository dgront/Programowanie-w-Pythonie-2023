import math
import random

k = 7.0
a1 = 17
A1 = 8
wynik1 = a1 + A1 * 7 - 4.16/3.12
wynik2 = (wynik1 + 2.) / wynik1

napis2 = "8"
napis = "7.5"
w = 16 + float(napis)
print(str(w) + " ala")
print(math.sqrt(16))
l = True
l2 = False
print("alternatywa:",l or l2)
print("koniungcja:",l and (not l2))

not (l or l2)
(not l) and (not l2)

napis = """Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie."""
l = 14
if l > 7:
    # print(napis)
    if l % 2 == 0:
        print("i na dodatek\n\tjest parzyste")
    print("Ala ma kota")


N = 8
epsilon = 0.0001

if N > 0:
    pass

# Tu bardzo interesujący opis, co robi pętla poniżej
suma = 0
for i in range(1, N):
    for j in range(1, N):
        suma = i + j
        # print("tutaj")
        if suma > 10:
            continue
        # print("a tu dalej:",i, j, suma)

# ----------formatowanie w print
pi = "Ludolfina:"
print("Kilka faktów o liczbie pi znanej jako: %s %5.3f %05d" % \
      (pi, math.pi, math.pi))

died = True
while True:
    print("Syzyfowa praca")
    if died:
        break

for i in range(N):
    f = i + 0.5
    print("%2d %3f" % (i,f), end="")

print()
for i in range(20):
    # print(random.random())
    if random.random() < 0.1:
        print("O", end="")
    else:
        print("#", end="")

print("\n\n\n\n\n\n\n")
# N=5
for i in range(1,N+1):
    for j in range(i):
        print("#", end="")
    print()

# wczytywanie danych wejściowych z klawiatury, rzut napisu na liczbę całkowitą
rok_1 = input("podaj rok początkowy:")
rok_2 = input("podaj rok końcowy:")
rok_1 = int(rok_1)
rok_2 = int(rok_2)
print(rok_1, rok_2)
# zamiana zmiennych miejscami

if rok_2 < rok_1:
    tmp = rok_1
    rok_1 = rok_2
    rok_2 = tmp

print("Wybrano lata od %d do %d" % (rok_1, rok_2))

