import requests, re

# Adres strony, która podaje 250 najpopularniejszych filmów
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
out = requests.get(url)                     # --- pobrana strona
wzorzec = "title/tt\d+/"                    # wyrażenie regularne wyszukujące kod filmu
wyniki = re.findall(wzorzec, out.text)      # wyniki to kody filmów
unikalne_filmy = set()                      # zbieramy tylko unikalne
for k in wyniki:                            # pętla po fragmentach pasujących do wzorcach
    kod_filmu = k.split("/")[1]             # wybieramy kod filmu
    unikalne_filmy.add(kod_filmu)

aktorzy = {}                                # Słownik do zliczania aktorów
for kod_filmu in list(unikalne_filmy):
    print("Pobieram:",kod_filmu)
    # --- kod filmu wklejamy do linku aby pobrać stronę z obsadą filmu
    # https://www.imdb.com/title/tt0111161/fullcredits/?ref_=tt_cl_sm
    url = "https://www.imdb.com/title/" + kod_filmu + "/fullcredits/?ref_=tt_cl_sm"
    out = requests.get(url).text
    wzorzec = "alt=\"(.+?)\" title=\".+?\" "
    obsada = re.findall(wzorzec,out)
    for aktor in obsada:
        if aktor in aktorzy:
            aktorzy[aktor] +=1
        else:
            aktorzy[aktor] = 1

# --- sortujemy wyniki i drukujemy 10 najpopularniejszych
wyniki = sorted(aktorzy.items(), key=lambda item: item[1], reverse=True)
for w in wyniki[:10]:
    print(w)


