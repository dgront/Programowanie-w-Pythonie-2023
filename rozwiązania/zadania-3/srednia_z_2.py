plik = open("plik.txt", "r")
# Plik "plik.txt" powinien wyglądać następująco:
# 0.22387513578688933 0.4263556687902609
# 0.07153576376523008 0.7496693057508832
# 0.9425084596887234 0.6291578833934092

suma = 0
counter = 0
for linia in plik:                  # tu iterujemy po liniach z pliku
    linia_obcieta = linia.strip()   # obcinamy białe znaki z końców
    if len(linia_obcieta) == 0: continue    # puste linie ignorujemy
    wyrazy = linia_obcieta.split()  # dzielimy linię na wyrazy
    if len(wyrazy) < 2: continue    # jak nie ma 2 wyrazów, to nie ma 2 kolumny
    if wyrazy[1].isnumeric():       # czy w 2 kolumnie jest liczba?
        suma += float(wyrazy[1])
        counter += 1
print(suma / counter)
