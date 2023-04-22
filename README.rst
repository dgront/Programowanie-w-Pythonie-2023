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
#. Korzystając z podwójne zagnieżdżonej pętli wydrukuj na ekranie tabliczkę mnożenia od 1 do 10


2. Listy i słowniki
--------------------------------------

#. Stwórz pustą listę i wypełnij ją dziesięcioma zerami
#. Stwórz listę liczb od 0 do 10 włącznie
#. W powyższej liście zamień miejscami elementy 5-ty i 7-my
#. Wylosuj 20 liczb i dopisz do listy
#. Zadeklaruj zmienną napisową zawierającą słowo "konstantynopolitańczykowianeczka"; stwórz pętlę, która po kolei
   wypisze wszystkie litery tego wyrazu.
#. Wypisz litery powyższego wyrazu w odwrotnej kolejności (od ostatniej do pierwszej).
#. Wypisz 10 losowych liter z tego wyrazu.
#. Stwórz słownik zawierający wartość ``12`` dla klucza ``"C"``.
#. Dodaj do słownika wartości ``14`` i ``16`` odpowiednio dla kluczy ``"N"`` i ``"O"``.
#. Wydrukuj na ekranie wszystkie klucze z tego słownika.
#. (*) Stwórz dwie listy: ``lista_i = []``, do której wstawisz ``K`` (np ``K=20``) losowych liczb całkowitych z przedziału :math:`[0,N)`,
   oraz ``lista_x = []``,do której wstawisz N losowych liczb rzeczywistych. Następnie policz sumę liczb wskazaną indeksami.
   Przykład: Dla ``K=5`` i ``N=3`` możemy wylosować ``lista_i = [0, 1, 2, 1, 1]`` i ``lista_x = [0.34, 0.12, 0.98]``. Wtedy
   poprawna suma to ``0.34 + 0.12 + 0.98 + 0.12 + 0.12 = 1.68``

3. Przetwarzanie plików
--------------------------------------

#. Utwórz plik "data.txt", zapisz do niego 10 liczb losowych i zamknij go.
#. Wczytaj plik "data.txt" i wydrukuj zawartość na ekranie
#. Wczytaj plik "data.txt" linia po linii i wydrukuj na ekranie te linie,
   które zaczynają się na 1
#. Wczytaj plik "data.txt" i oblicz średnią z liczb w tym pliku
#. Wczytaj plik "data.txt" linia po linii i oblicz średnią z liczb w tym pliku
#. Wczytaj plik "lotr1.txt" linia po linii i wypisz liczbę wyrazów w każdej linijce; plik ten znajduje się `tutal <http://bioshell.pl/~dgront/lotr1.txt>`_
#. (*) policz, który wyraz powtarza sie najczęściej w "Lord of the rings"
#. Wydrukuj pliki z bieżącego katalogu
#. Wydrukuj bieżący katalog
#. (*) policz, ile plików o rozszerzeniu ``".jpg"`` jest we wszystkich podkatalogach
#. (**) napisz program, który zlicza wszystkie pliki we wszystkich podkatalogach, grupując je wg rozszerzenia; wynikiem
   działania programu powinna być tabelka wyglądająca np tak : ``"JPG": 124, "PNG": 34, "EXE": 2, "TXT": 17``

4. Własne funkcje
--------------------------------------

#. Stwórz funkcję, która dodaje dwie liczby
#. Stwórz funkcję, która rozwiązuje równanie kwadratowe;
   jej argumentami powinny być współczynniki a, b i c równania.
#. (*) Napisz funkcję, która szyfruje wiadomość wg szyfru Cezara. Argumentami tej funkcji powinny być:
   szyfrowana wiadomość (string) oraz przesunięcie alfabetu (liczba całkowita). Zauważ, że ta sama funkcja
   może być wykorzystywana do odczytywania szyfrogramów, kiedy przesunięcie jest ujemne.

5. Przydatne moduły
--------------------------------------

a. praca z plikami XLS
++++++++++++++++++++++++

#. zainstaluj moduł openpyxl
#. stwórz arkusz w którego kolumnie A będzie 10 kolejnych liczb całkowitych
#. stwórz arkusz z tabliczką mnożenia
#. stablicuj epitrochoidę; krzywa ta zadana jest równaniem parametrycznym:

    x(t) = (R+r) * cos(t) - h * cos((R+r)/r * t)
    y(t) = (R+r) * sin(t) - h * sin((R+r)/r * t)

    zapisz w arkuszu: w kolumnie A wartości t od 0 do 5.0 co 0.01, w kolumnie B wartości
    x(t) a w kolumnie C y(t), następnie zrób w Excelu wykres y(x)
#. Model Lotki-Voltery

b. wykresy z matplotlib
++++++++++++++++++++++++
#. zainstaluj moduł matplotlib
#. zrób wykres funkcji sinus; w tym celu:wpisz do
  - wpisz do listy ``x`` liczby rzeczywiste od 0 do 6.28 co 0.01
  - wpisz do listy ``y`` wartości sin(x)
  - zrób wykres
#. zrób wykres epitrochoidy, korzystając z biblioteki matplotlib

6. Złożone struktury danych
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

7. argsy i kwargsy, sprawdzanie typów
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

8. webscraping i przetwarzanie tekstu
--------------------------------------
#. Napisz wyrażenie regularne, które weryfikuje poprawność formatu: kod pocztowy, nr PESEL, NIP
#. Zainstaluj pakiety: requests, BeautifulSoup
#. Pobierz dowolną stronę internetową korzystając z modułu requests i nagraj ją jako tekst
#. Wyszukaj w tekście strony internetowej wszystkie obrazki, czyli elementy zaczynające się na "<img" i końćzące się na "/img>"
   Rozwiąż ten problem dwoma sposobami: korzystając z wyrażeń regularnych oraz modułu BeautifulSoup
#. Wytnij URL każdego obrazka, pobierz go i nagraj do oddzielnego pliku
#. Pobierz listę 250 najlepszych filmów ze strony "https://www.imdb.com/chart/top/?ref_=nv_mv_250" i policz średni ranking tych filmów
#. (*) Pobierz listę 250 najlepszych filmów, pobierz listę aktorów każdego z filmów i sprawdź, czyje nazwisko pojawia się najczęsciej


9. GUI
#. Utwórz minimalny działający program: główne okno i pętlę aplikacji
#. dodaj guzik do okna; dodaj do niego jakąś akcję (np. po kliknięciu program drukuje na ekran jakiś napis)
#. Napisz program "kalkulator": powinien mieć  guziki na podstawowe działania (*,+, /, +). Do obliczania wyniku użyj funkcji eval()
