klucz = 3  # --- o tyle znaków przesuwamy alfabet
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = "TAJNAWIADOMOSC"
for l in list:
    # --- znajdujemy indeks litery i przesuwamy
    index = alfabet.find(l) + klucz
    # trzeba zawinąć do długości alfabetu!
    index = index % len(alfabet)
    print(alfabet[index], end="")