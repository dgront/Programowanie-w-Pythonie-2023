import random
from math import sin

# ---------- na początek zdefiniujmy jakieś funkcje
def kwadrat(x): return x*x
def minus(x): return -x


# -------------------------------- opowieść o zmiennych lokalnych i globalnych
sum = 0                 # --- sumujemy do zmiennej globalnej

def mod_list_sum(liczby, operacja):
    global sum          # --- dostep do zmiennej globalnej
    for i in range(len(liczby)):
        liczby[i] = operacja(liczby[i])
        sum += liczby[i]
    return sum

N = 10
liczby = [random.random() for i in range(N)]

print(liczby)
x = mod_list_sum(liczby, sin)
print(liczby, x, sum)

# -------------------------------- sortowanie z dziwną funkcją
s = liczby.sort()               # --- najpierw sortowanie "normalne"
print(liczby)

def ostatnia_cyfra(x):          # --- funkcja zwracająca ostatnią cyfrę w zapisie dziesiętnym liczby
    s = str(x)
    return int(s[-1])

print(ostatnia_cyfra(0.5611))           # --- sprawdźmy, czy działa
liczby.sort(key=ostatnia_cyfra)         # --- sortowanie po ostatniej cyfrze
print(liczby)


# -------------------------------- praktyczny przykład: sortowanie słownika
s = {"Ala":2, "Ola":7, "Zuza": 5}       # --- jakiś tam słownik
def sortuj_po_wart(klucz):              # --- funkcja sortująca: zwraca wartość dla klucza
    return s[klucz]

print(sortuj_po_wart("Ola"))            # --- sprawdźmy, że funkcja działa
# --- sprawdźmy, czy sortuje poprawnie
klucze_posort = sorted(s.keys(), key=sortuj_po_wart)
print(klucze_posort)

# -------------------------------- sortowanie liczb z lambdą
# --- funkcja w jednej linijce
def ostatnia_cyfra_oneliner(x): return int(str(x)[-1])
# --- lambda to taka uproszczona funkcja bez nazwy; można ją zapakować do zmiennej
f = lambda x: int(str(x)[-1])

print(ostatnia_cyfra_oneliner(0.56113)) # --- sprawdźmy, że funkcja działa
print(liczby)
liczby.sort(key=lambda x: int(str(x)[-1]))
print(liczby)

# ---- przekaż lambdę jako argument do funkcji
mod_list_sum(liczby, f)
print(liczby)