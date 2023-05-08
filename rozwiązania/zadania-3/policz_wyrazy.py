import operator
do_usuniecia = "<>,.?!@#$%^&*()_+=-`~\""

slowa = {}                              # pusty słownik na zliczenia wyrazów
with open("lotr1.txt") as plik:         # otwórz plik
    for linia in plik:                  # linijka po linijce
        wyrazy = linia.strip().split()
        for w in wyrazy:                # pętla po wyrazach
            # tu obcinamy znaki interpunkcyjne z końca wyrazu
            for znak in do_usuniecia:
                w = w.replace(znak, "")
            if w in slowa:              # Aktualizuj licznik
                slowa[w] += 1
            else:                       # lub wstaw do slownika
                slowa[w] = 1

# sortowanie wynikowego słownika
def kolejnosc(w):
    return slowa[w]
posortowane = sorted(slowa.items(), key=kolejnosc, reverse=True)
print(posortowane[:10])
# ---- inny sposób sortowania slownika
posortowane = sorted(slowa.items(), key=operator.itemgetter(1), reverse=True)
print(posortowane[:10])
