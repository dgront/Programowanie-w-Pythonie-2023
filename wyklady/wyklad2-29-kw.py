# ---------- slice czyli plasterek z listy
l = [1,2,3,4,5,6]
print(l[:3])

# ---------- sortowanie listy
import random
l = [1, 2, 3, 4, 5, 6]
random.shuffle(l)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
#----------- zadanie o listach: totolotek ----------
import random

N = 1000

lista = []
for i in range(49):
     lista.append(0)
kule = []
for i in range(49):
     kule.append(i+1)

for i in range(N):
     random.shuffle(kule)
     for j in range(6):
         r = kule[j]
         lista[r-1] += 1
for i in range(len(lista)):
     print(lista[i])

#-------- krótko w słownikach --------
slownik = {}
slownik[10] = "10.1"
slownik[12] = 10.2
slownik[14] = 10.3
slownik[9] = 10.4
slownik["9 i 3/4"] = 10.5
print(slownik)

#-------słownik: zliczanie liter w inwokacji ------
inwokacja = """Litwo! Ojczyzno moja! ty jesteś jak zdrowie. Ile cię
trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w
całej ozdobie. Widzę i opisuję, bo tęsknię po tobie. Panno Święta, co
jasnej bronisz Częstochowy. I w Ostrej świecisz Bramie! Ty, co gród
zamkowy. Nowogródzki ochraniasz z jego wiernym ludem!"""

zliczenia = {}
for litera in inwokacja:
#    if not (litera in zliczenia):
     if litera not in zliczenia:
         zliczenia[litera] = 1
     else:
         zliczenia[litera] += 1
# --- tak drukujemy klucze
print(zliczenia.keys())
# --- tak drukujemy same wartości
print(zliczenia.values())
# --- a tak pary klucz-wartość - jako dwutuple
print(zliczenia.items())

#---------- tabliczka mnożenia w liście dwuwymiarowej -------------
tabliczka = []
for i in range(10):
     wiersz = []
     for j in range(10):
         wiersz.append((i+1)*(j+1))
     tabliczka.append(wiersz)

for w in tabliczka:
     print(w)

#--------- konstrukcja "for cos w czymś" -------------

wyrazy = ["Ala", "ma", "kota"]
for li in wyrazy: print(li)

napis = "asdfghjklxcvbnmsdfghj"
for i in range(len(napis)):
     print(napis[i])

for litera in napis:
     print(litera)



