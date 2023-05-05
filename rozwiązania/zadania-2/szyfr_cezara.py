szyfr = ".ABCDEFGHIJKLMNOPQRTSUVWYXYZ"
tajna_wiadomość = "ave.cezar.moriture.de.salutant"
zaszyfrowana_w = ""

klucz = 2           # --- o tyle znaków przesuwamy alfabet
for litera in tajna_wiadomość:
    nr = szyfr.find(litera.upper()) # --- znajdujemy indeks litery
    index = nr + klucz              # ---  i przesuwamy o klucz
    index = index % len(szyfr)      # --- trzeba zawinąć do długości alfabetu!
    zaszyfrowana_lit = szyfr[index]
    zaszyfrowana_w += zaszyfrowana_lit
print(zaszyfrowana_w)

klucz = -2
deszyfr = ""
for litera in zaszyfrowana_w:
    nr = szyfr.find(litera.upper())
    zaszyfrowana_lit = szyfr[(nr + klucz) % len(szyfr)]
    deszyfr += zaszyfrowana_lit
print(deszyfr)