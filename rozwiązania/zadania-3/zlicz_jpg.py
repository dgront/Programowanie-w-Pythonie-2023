import os

#liczymy ile jest WSZYSTKICH plików .jpg
suma = 0
lista_plikow = []
for cos in os.walk("."):
    print("w katalogu",cos[0],"są pliki:",cos[2])
    for plik in cos[2]:
        if plik.endswith(".jpg"):
            suma += 1
            pelna_nazwa = os.path.join(cos[0], plik)
            lista_plikow.append(pelna_nazwa)
print(lista_plikow)
