# UWAGA! Plik pracownik.py musi być w tym samym katalogu, co ten plik
from pracownik import Pracownik, Kierownik

p = Pracownik("Zupa", "Grzybowa")
k = Kierownik("Johny", "Nopapa")
# trzech pracowników na dwóch kierowników - niezły wynik
personel = [k, p, p, p, k]

# --- sortowanie obiektów z wyrażeniem lambda
personel.sort(key=lambda o: o.nazwisko())
# --- wydruk personelu
for i in personel:
    print(i)


