# ------------ funkcje
import random


def funkcja_pusta():
    pass

def funkcja():
    print("przybij piątkę")
    x = 2 * 2 + 1
    return x

def funkcja_xy():
    x = 2 * 2 + 1
    y = x * 7
    return (x, y)

def pomnoz(x, y):
    return x*y

print(funkcja())
x, y = funkcja_xy()

# ------------ operacje na napisach
txt = "Ala ma kota     a Zuza ma psa"
csv = "2,3,,4,5"
wyrazy = txt.split()
cyfry = csv.split(',')
print(wyrazy,cyfry)

# ------------ pliki
plik = open("../dane/plik.txt")

# ------------ suma z drugiej kolumny
suma = 0
for linia in plik:  # tu iterujemy po liniach z pliku
    wyrazy = linia.strip().split()
    suma += float(wyrazy[1])
print(suma)
tresc = plik.read()
linie = tresc.split('\n')
print(len(tresc))
print(tresc[:100])

# --- wczytanie wszystkich linii
plik.close()
plik = open("../dane/plik.txt")
lista_linii = plik.readlines()
print(lista_linii)
plik.close()

# --- pętla po liniach w pliku
with open("../dane/plik2.txt","w") as plik2:
    for i in range(10):
        r = random.random()
        print(r)
        plik2.write(str(r))
        if i % 2 == 0:
            plik2.write("\n")
        else:
            plik2.write(" ")
        # plik2.write("%6.4f\n" % (r))
# --- TUTAJ Python zamyka plik

# --- operacje na systemie plików
import glob, shutil, os.path
p = "C:" + "/" + "Dektop"
p = os.path.join("C:","Desktop")
print(p)
lista_plikow = glob.glob("../**/p*.txt", recursive=True)
for nazwa in lista_plikow:
    w = nazwa.split("/")
    nowa_nazwa = "kopia_" + w[-1]
    print(nazwa, nowa_nazwa)
    shutil.copy(nazwa, nowa_nazwa)

