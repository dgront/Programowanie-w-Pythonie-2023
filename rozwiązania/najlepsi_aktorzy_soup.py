import requests
from bs4 import BeautifulSoup

# Adres strony, która podaje 250 najpopularniejszych filmów
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
out = requests.get(url)                         # --- pobrana strona
soup = BeautifulSoup(out.text,"html.parser")    # --- strona przeparsowana

kody_filmow = []                                # --- lista kodów filmów
# --- Pierwsza tabela (element table) zawiera listę filmów
# --- idziemy w pętli po wszystkich wierszach (elementy "tr") tabeli
for wiersz in soup.table.find_all("tr"):
    # --- z każdego wiersza wyjmujemy element z tytułem
    w = wiersz.find_all("td", class_="titleColumn")
    for wi in w:
        href = wi.a["href"]
        kod_filmu = href.split("/")[2]
        kody_filmow.append(kod_filmu)
# --- Wybraliśmy kody filmów, np "tt0074958"

aktorzy = {}
for kod_filmu in list(kody_filmow):
    print("Pobieram:",kod_filmu)
    # --- kod filmu wklejamy do linku aby pobrać stronę z obsadą filmu
    # https://www.imdb.com/title/tt0111161/fullcredits/?ref_=tt_cl_sm
    url = "https://www.imdb.com/title/" + kod_filmu + "/fullcredits/?ref_=tt_cl_sm"
    out = requests.get(url)
    soup = BeautifulSoup(out.text,"html.parser")
    obsada = soup.find("table",class_="cast_list")
    # --- pobieramy obrazki, bo w podpisie jest nazwisko aktora
    for obrazek in obsada.find_all("img"):
        aktor = obrazek["alt"]
        if aktor in aktorzy:
            aktorzy[aktor] += 1
        else:
            aktorzy[aktor] = 1

# --- sortujemy wyniki i drukujemy 10 najpopularniejszych
wyniki = sorted(aktorzy.items(), key=lambda item: item[1], reverse=True)
for w in wyniki[:10]:
    print(w)
