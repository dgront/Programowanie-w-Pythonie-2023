import urllib.request

# ---- pobierz stronę z internetową ze spisem filmów
adres = 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc'
with urllib.request.urlopen(adres) as response:
    html = response.read()
#
# ---- zapisz do pliku
    with open("strona.html","w") as plik:
       plik.write(str(html))

# ---- wczytaj z pliku do tekstu
hmlt_po_wczytaniu = open("strona.html").read()
# ---- załaduj html do obiektu  BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(hmlt_po_wczytaniu, 'html.parser')

# ---- znajdz wszystkie elementy klasy "userRatingValue"
wynik = soup.find_all("span", class_="userRatingValue")
numery_tt = []
for wi in wynik:
    wi_napis = str(wi)
    # ---- z każdego elementu wydłub wartość przy "data-tconst"
    # -zapakuj do listy wszystkie numery "tt"
#    numery_tt.append(wi_napis.replace("=",' ').split()[4].replace("\"",""))
    numery_tt.append(wi_napis.split("\"")[3])
print(numery_tt)

# --- pętla po filmach (numerkach 'tt')
slownik = {}
for numerek_tt in  numery_tt[:]:
# ---- zbieranie obsady z filmu
    url = "https://www.imdb.com/title/" +numerek_tt+"/fullcredits/?ref_=tt_cl_sm"
    print(url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup2 = BeautifulSoup(html, 'html.parser')
        wynik = soup2.find_all("td", class_="primary_photo")
        for w in wynik:
            aktor = str(w).split("\"")
            a = aktor[5]
            if a in slownik:
                slownik[a] += 1
            else:
                slownik[a] = 1
# ---- tu sortujemy słownik
import operator
posortowane = sorted(slownik.items(), key=operator.itemgetter(1), reverse=True)
print(posortowane[:10])