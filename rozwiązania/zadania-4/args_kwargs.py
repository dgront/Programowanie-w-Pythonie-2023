# ---- Funkcja licząca sumę liczb z listy
def suma(val:list):
    suma = 0
    for v in val:
        suma += v
    return suma

# print(suma([7,12, 12, 7, 18, 5]))

# ---------- Lista rozpakowana ("argsy")
def suma_liczb(potega, *args):
    suma = 0
    for liczba in args:
        print("v=",liczba)
        suma += liczba**potega
    return suma**(1.0/potega)

# print( suma_liczb(2,3,4,5) )

# ---------- Argumenty nazwane - rozpakowany słownik ("kwargsy")
slownik = {"A":3, "B":7}
# print(slownik)

def co_jemy(*goscie, **kwargs):
    print("na obiedzie są:",goscie)
    print("jadlospis",kwargs)

co_jemy("Ola", "Ala")
co_jemy("Ola", "Ala", zupa="grzybowa", drugie="kotlet", ile_gosci=6)

# ---------- kwargs w funkcjach standardowych Pythona
plik=open("zupa.txt","w")
print(2,3,4,5,6,end="%%\n", sep="-", file=plik)
plik.close()

lista = [ (1,1), (3,1), (5,4), (3,3)]
print(sorted(lista, reverse=True, key=lambda krotka:krotka[1]))


# ---------- sprawdzanie typu

def suma_liczb_n(*args, **kwargs):

    if isinstance(args,list):
        print("args jest listą")
    elif isinstance(args, tuple):
        print("args jest krotką")
    else:
        print("nie mam pojęcia czym jest args")


    if isinstance(args[0],list) or isinstance(args[0],tuple):
        print("args[0] is a list:",args[0] )
        wartosci_do_sumowania = args[0]
    else:
        print(args[0],"is not a list")
        wartosci_do_sumowania = args

    fctor = kwargs.get("factor", 1.0)
    powr = kwargs.get("power", 2.0)

    suma = 0
    for liczba in wartosci_do_sumowania:
        suma += (fctor*liczba)**powr

    return suma ** (1.0 / powr)

# print(suma_liczb_n(1,2,3,4,5, factor=2.5, power=2))
# print(suma_liczb_n(1,2,3,4,5, power=3))
# print(suma_liczb_n(1,2,3,4,5, factr=2.5))       # --- UWAGA - literówka!!!!
print(suma_liczb_n(1,2,3,4,5))

print(suma_liczb_n( [1,2,3, 4, 5, 6] ))
print(suma_liczb_n( 1,2,3,4,5,6 ))
print(suma_liczb_n( 1,2,3,4,5,6 ))

