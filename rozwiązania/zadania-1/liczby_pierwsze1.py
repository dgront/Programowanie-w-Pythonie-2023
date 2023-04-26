N = 20
for kandydat in range(2,N+1):
    czy_jest_pierwsza = True
    for dzielnik in range(2,kandydat):
        reszta = kandydat % dzielnik
        if reszta == 0:
            czy_jest_pierwsza = False
            break
        else:
            print("%d niepodzielna przez %d" % (kandydat, dzielnik))
    if czy_jest_pierwsza:
        print("%d jest pierwsza" % (kandydat))