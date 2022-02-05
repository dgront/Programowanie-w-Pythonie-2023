import operator

slowa = {}                      # pusty słownik na zliczenia wyrazów
with open("lotr1.txt") as plik: # otwórz plik
    for linia in plik:          # linijka po linijce
        wyrazy = linia.strip().split()
        for w in wyrazy:        # pętla po wyrazach
            # tu obcinamy znaki interpunkcyjne z końca wyrazu
            n = len(w)          # liczba znaków w wyrazie
            if not w[n-1].isalpha():
                w = w[:n-1]
# Inny sposób usuwania znaków z końca - z ujemnym indeksowaniem znaków
#            if not w[-1].isalpha(): w = w[:-2]
            if w in slowa:      # Aktualizuj licznik
                slowa[w] += 1
            else:               # lub wstaw do slownika
                slowa[w] = 1

# sortowanie wynikowego słownika
posortowane = sorted(slowa.items(), key=operator.itemgetter(1), reverse=True)
print(posortowane[:10])
