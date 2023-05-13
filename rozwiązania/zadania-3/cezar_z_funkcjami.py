
szyfr = ".ABCDEFGHIJKLMNOPQRTSUVWYXYZ"
tajna_wiadomość = "ave.cezar.moriture.de.salutant"
zaszyfrowana_w = ""

def cezar(tekst, klucz):
    """To jest dokumentacja funkcji cezar.

    Funkcja działa jeszcze lepiej, niż sam Juliusz.
    """

    zaszyfrowana_w = ""
    for litera in tekst:
        nr = szyfr.find(litera.upper())  # --- znajdujemy indeks litery
        index = nr + klucz  # ---  i przesuwamy o klucz
        index = index % len(szyfr)  # --- trzeba zawinąć do długości alfabetu!
        zaszyfrowana_lit = szyfr[index]
        zaszyfrowana_w += zaszyfrowana_lit
    print(zaszyfrowana_w)
    return zaszyfrowana_w

zakodowane = cezar(tajna_wiadomość, 2)
odkodowane = cezar(zakodowane, -2)
