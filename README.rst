Programowanie w Pythonie 2023
=============================

0. Zmienne i operacje na nich
--------------------------------------

1. Pętle i warunki
--------------------------------------

#. Zadeklaruj zmienną ``N=15`` a następnie wydrukuj N znaków ``#`` korzystając z pętli
#. Korzystając z pętli wydrukuj N znaków: ``_`` dla parzystych
   a ``#`` dla nieparzystych wartości indeksu pętli
#. Powyższy wydruk powinien być w jednej linii
#. Korzystając z podwójne zagnieżdżonej pętli wydrukuj na ekranie prostokąt NxN znaków ``#``
#. Korzystając z podwójne zagnieżdżonej pętli wydrukuj na ekranie tabliczkę mnożenia od 1 do 10  `[rozwiązanie] <./rozwiązania/zadania-1/tabliczka.py>`_
#. Narysuj choinki o różnych kształtach (trójkąty złożone ze znaków ``#``) `[choinka lewa] <./rozwiązania/zadania-1/choinka_prawa.py>`_ `[choinka lewa] <./rozwiązania/zadania-1/choinka_lewa.py>`_
#. Oblicz średnią z N liczb losowych z rozkładu płaskiego [0,1) `[rozwiązanie] <./rozwiązania/zadania-1/srednia.py>`_
#. Oblicz liczbę PI metodą Monte Carlo `[rozwiązanie] <./rozwiązania/zadania-1/liczba_pi.py>`_
#. Napisz program, który sprawdza, czy podany rok jest przestępny; lata przestępne to te, które dzielą się przez 4 a nie dzielą przez 100 albo dzielą się przez 400.
#. (*) Wydrukuj liczby pierwsze z przedziału [2,N]. Liczba pierwsza to taka, która dzieli się tylko przez jeden i samą siebie; dzieląc K (liczbę-kandydata) przez liczby [3,N-1] wszystkie dzielenia powinny dać niezerową resztę `[rozwiązanie z flagą] <./rozwiązania/zadania-1/liczby_pierwsze1.py>`_


2. Listy i słowniki
--------------------------------------

#. Stwórz pustą listę i wypełnij ją dziesięcioma zerami
#. Stwórz listę liczb od 0 do 10 włącznie
#. W powyższej liście zamień miejscami elementy 5-ty i 7-my
#. Wylosuj 20 liczb i dopisz do listy
#. Zadeklaruj zmienną napisową zawierającą słowo "konstantynopolitańczykowianeczka"; stwórz pętlę, która po kolei
   wypisze wszystkie litery tego wyrazu.
#. Wypisz litery powyższego wyrazu w odwrotnej kolejności (od ostatniej do pierwszej). `[rozwiązanie] <./rozwiązania/zadania-2/litery_od_tylu.py>`_
#. Wypisz 10 losowych liter z tego wyrazu.  `[rozwiązanie] <./rozwiązania/zadania-2/losowe_litery_z_wyrazu.py>`_
#. Stwórz słownik zawierający wartość ``12`` dla klucza ``"C"``.
#. Dodaj do słownika wartości ``14`` i ``16`` odpowiednio dla kluczy ``"N"`` i ``"O"``.
#. Wydrukuj na ekranie wszystkie klucze z tego słownika.

#. **Suma wg. indeksów** Stwórz dwie listy: ``lista_i = []``, do której wstawisz ``K`` (np ``K=20``) losowych liczb całkowitych z przedziału :math:`[0,N)`,
   oraz ``lista_x = []``,do której wstawisz N losowych liczb rzeczywistych. Następnie policz sumę liczb wskazaną indeksami.
   Przykład: Dla ``K=5`` i ``N=3`` możemy wylosować ``lista_i = [0, 1, 2, 1, 1]`` i ``lista_x = [0.34, 0.12, 0.98]``. Wtedy
   poprawna suma to ``0.34 + 0.12 + 0.98 + 0.12 + 0.12 = 1.68``

#. **Epitrochoida**
   Zadeklaruj dwie puste listy: `X` oraz `Y`; wstaw do nich kolejne wartości `xt` i `yt` wygenerowane wg wzoru:

    x(t) = (R+r) * cos(t) - h * cos((R+r)/r * t)

    y(t) = (R+r) * sin(t) - h * sin((R+r)/r * t)

   Narysuj wykres Y(X) korzystając z biblioteki Matplotlib. `[rozwiązanie] <./rozwiązania/zadania-2/epitrochoida.py>`_

#. **Szyfr Cezara**
   to jedna z najprostszych technik szyfrowania, w której każda litera tekstu jawnego (niezaszyfrowanego)
   zastępowana jest inną, oddaloną od niej o stałą liczbę pozycji w alfabecie. Napisz program, który szyfruje a następnie
   deszyfruje wiadomości  `[rozwiązanie] <./rozwiązania/zadania-2/szyfr_cezara.py>`_


3. Przetwarzanie plików
--------------------------------------

#. Utwórz plik "data.txt", zapisz do niego 10 liczb pseudolosowych całkowitych z przedziału [1,10] i zamknij go. `[rozwiązanie] <./rozwiązania/zadania-3/plik_z_losowymi10.py>`_
#. Wczytaj plik "data.txt" i wydrukuj zawartość na ekranie
#. Wczytaj plik "data.txt" linia po linii i wydrukuj na ekranie te linie,
   które zaczynają się na 1
#. Wczytaj plik "data.txt" i oblicz średnią z liczb w drugiej kolumnie tego pliku. Upewnij się, że dane są poprawne `[rozwiązanie] <./rozwiązania/zadania-3/srednia_z_2.py>`_
#. Wczytaj plik "data.txt" i oblicz średnią z wszystkich liczb w tym pliku. Pamiętaj, aby przejśc w pętli po wszystkich liczbach z każdego wiersza `[rozwiązanie] <./rozwiązania/zadania-3/srednia_z_pliku.py>`_
#. Wczytaj plik "lotr1.txt" linia po linii i wypisz liczbę wyrazów w każdej linijce; plik ten znajduje się `tutal <http://bioshell.pl/~dgront/lotr1.txt>`_
#. (*) policz, który wyraz powtarza sie najczęściej w "Lord of the rings" `[rozwiązanie] <./rozwiązania/zadania-3/policz_wyrazy.py>`_
#. Wydrukuj pliki z bieżącego katalogu
#. Wydrukuj bieżący katalog
#. (*) policz, ile plików o rozszerzeniu ``".jpg"`` jest we wszystkich podkatalogach  `[rozwiązanie] <./rozwiązania/zadania-3/zlicz_jpg.py>`_
#. (**) napisz program, który zlicza wszystkie pliki we wszystkich podkatalogach, grupując je wg rozszerzenia; wynikiem
   działania programu powinna być tabelka wyglądająca np tak : ``"JPG": 124, "PNG": 34, "EXE": 2, "TXT": 17``

4. Własne funkcje
--------------------------------------

#. Stwórz funkcję, która dodaje dwie liczby
#. Stwórz funkcję, która rozwiązuje równanie kwadratowe;
   jej argumentami powinny być współczynniki a, b i c równania.
#. (*) Napisz funkcję, która szyfruje wiadomość wg szyfru Cezara. Argumentami tej funkcji powinny być:
   szyfrowana wiadomość (string) oraz przesunięcie alfabetu (liczba całkowita). Zauważ, że ta sama funkcja
   może być wykorzystywana do odczytywania szyfrogramów, kiedy przesunięcie jest ujemne.  `[rozwiązanie] <./rozwiązania/zadania-2/cezar_z_funkcjami.py>`_

5. praca z plikami XLS
--------------------------------------

#. zainstaluj moduł openpyxl
#. stwórz arkusz w którego kolumnie A będzie 10 kolejnych liczb całkowitych `[rozwiązanie] <./rozwiązania/zadania-4/wexelu_1.py>`_
#. stwórz arkusz z tabliczką mnożenia `[rozwiązanie] <./rozwiązania/zadania-4/tabliczka_w_exelu.py>`_

6. argsy i kwargsy, sprawdzanie typów
--------------------------------------
#. Stwórz funkcję o zmiennej liczbie argumentów, która liczy średnią z podanych liczb; poniższe wywołania powinny się udać:
  - srednia(1, 2)
  - srednia(1, 2, 3, 4, 5)
  - srednia(1, 2, 3, 5, 6, 7, 8)
#. Stwórz funkcję, która drukuje na ekranie napis, reprezentujący jeden element HTML. Pierwszym (pozycyjnym) argumentem
   tej funkcji powinien być typ elementu (np "div" lub "p"), po którym powinny następować argumenty nazwane, określające
   atrybuty HTML. I tak dla przykładu, wywołanie ``drukuj_html("div",id="el43", class="redborder")`` powinno wydrukować
   na ekranie: ``"<div id='el43' class='redborder'>"``
#. Stwórz funkcję, która policzy średnią z podanej listy liczb. Funkcja powinna zwracać ``6`` we wszystkich
   poniższych przypadkach:
      - srednia(1, 2, 3, 4, 5)
      - srednia([1, 2, 3, 4, 5])
      - srednia([(1,1), (2,1), (3,1), (4,1), (5,1)], column=0)
      - srednia([(1,1), (1,2), (1,3), (1,4), (1,5)], column=1)
   W tym celu wykorzystaj ``isinstance`` do sprawdzenia, jakiego typu jest argument ``args[0]``

 `[rozwiązania] <./rozwiązania/zadania-4/args_kwargs.py>`_

7. Złożone struktury danych
--------------------------------------
#. Zainicjuj listę 3x3
#. Stwórz listę 2D zawierającą tabliczkę mnożenia 10x10; wykorzystaj pętle
#. Napisz program rysujący zbiór Mandelbrota
#. (*) Policz unikalne tertapeptydy. W pliku ``chains_from_db-uniq10.fasta`` znajdziesz sekwencje
   białek, zapisane w następującym formacie:

        >6cgxA
        GCCSDPRCNYAHPAICGGAAGG
   gdzie linia zaczynająca się od ``>`` to nagłówek, który trzeba pominąć a ``GCCSDPRCNYAHPAICGGAAGG`` to owa sekwencja.
   Napisz program, który:

     - wczyta wszystkie sekwencje z pliku
     - każdy z napisów (sekwencji) podzieli na 4-ro literowe fragmenty ze skokiem co 1, np dla ``GCCSDPRCNYAHPAICGGAAGG``
       będą to ``GCCS``, ``CCSD``, ``CSDP`` itd.
     - zliczy, ile razy trafiła się każdy z różnych takich czteroliterowych wyrazów

8. webscraping i przetwarzanie tekstu
--------------------------------------
#. Zainstaluj pakiety: requests, BeautifulSoup
#. Pobierz dowolną stronę internetową korzystając z modułu requests i nagraj ją jako tekst `[rozwiązanie] <./rozwiązania/zadania-4/pobierz_strony.py>`_
#. Wyszukaj w tekście strony internetowej wszystkie obrazki, czyli elementy zaczynające się na "<img" i kończące się na "/img>"
   Rozwiąż ten problem dwoma sposobami: korzystając z wyrażeń regularnych oraz modułu BeautifulSoup `[rozwiązanie] <./rozwiązania/zadania-4/obrazki_na_stronie.py>`_
#. Pobierz listę 50 najlepszych filmów ze strony "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc" i policz średni ranking tych filmów
#. Pobierz listę 50 najlepszych filmów, pobierz listę aktorów każdego z filmów i sprawdź, czyje nazwisko pojawia się najczęsciej `[rozwiązanie] <./rozwiązania/zadania-4/najlepszy_aktor.py>`_

9. Przetwarzanie danych tabelarycznych: moduł Pandas
-----------------------------------------------------

#. Wczytaj plik w formacie CSV, np `[pokemon.csv] <./dane/pokemon.csv>`_
#. pobierz listę kolumn
#. pobierz wybraną kolumnę oraz wybrany wiersz (pole ``loc`` oraz ``iloc``)
#. pobierz wybrany element
#. znajdź Pokemona z najmniejszym BMI

10. GUI
---------
#. Utwórz minimalny działający program: główne okno i pętlę aplikacji
#. dodaj guzik do okna; dodaj do niego jakąś akcję (np. po kliknięciu program drukuje na ekran jakiś napis)
#. Napisz program "kalkulator": powinien mieć  guziki na podstawowe działania (*,+, /, +). Do obliczania wyniku użyj funkcji eval()
