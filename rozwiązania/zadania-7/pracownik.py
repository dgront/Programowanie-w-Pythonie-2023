class Pracownik:

    WYDRUK = "TABELA"
    OSTATNIE_ID_PRACOWNIKA = 0

    def __init__(self, name, surname):
        self.__id_prac = Pracownik.OSTATNIE_ID_PRACOWNIKA + 1
        Pracownik.OSTATNIE_ID_PRACOWNIKA = self.__id_prac
        self.__name = name
        self.__surname = surname
        self.__wynagrodzenie = 0
        self.__urlop = 26
        self.partner = None

    def __str__(self):
        """Drukuje informację o pracowniku

W zależności od ustawienia globalnego pola Pracownik.WYDRUK,
drukowanie odbywa się w postaci tabelarycznje lub jako lista pól
        """
        if Pracownik.WYDRUK == "TABELA":
            ret_str = "%5d | %10s | %15s | %3d" % (self.__id_prac, self.__name, self.__surname, self.__urlop)
        else:
            partner_name = "BRAK"
            partner_surname = "BRAK"
            if self.partner != None :
                partner_name = self.partner.__name
                partner_surname = self.partner.__surname

            ret_str = """
    Imię:       %s
    Nazwisko:   %s
    nr ref:     %d 
    partner:    %s %s
            """ % (self.__name, self.__surname, self.__id_prac, partner_name, partner_surname)
        return ret_str

    def imie(self):
        """zwraca imię pracownika"""
        return self.__name

    def nazwisko(self):
        """zwraca imię nazwisko"""
        return self.__surname

    def __set_name(self, new_name):
        self.__name = new_name

    def id(self):
        return self.__id_prac


class Kierownik(Pracownik):

    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)
        self.__premia = 1000

    def __str__(self):
        s = super().__str__()
        return s + " KIEROWNIK"


if __name__ == "__main__":

    print("RÓZNE BZDURY")

    p1 = Pracownik("Zenobia", "Nowak")
    p2 = Pracownik("Gertruda", "Kowalska")
    personel = [p1, p2]

    Pracownik.WYDRUK = "TABELA"
#    Pracownik.WYDRUK = "LISTA"
    for p in personel:
        print(p)