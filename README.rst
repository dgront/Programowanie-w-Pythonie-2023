Programowanie w Pythonie 2022
=============================

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

4. Przydatne moduły
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
