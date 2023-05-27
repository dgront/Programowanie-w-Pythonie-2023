import math

# ---------- args-y i kwargs-y
def suma_w_potedze(*zupa, **grzybowa):
    # dozwolone_kwargsy = ["wykladnik"]

    wykl = grzybowa.get("wykladnik", 1)
    suma = grzybowa.get("wart_pocz", 1)
    for x in zupa:
        pass
        suma += math.pow(x,wykl)
    return suma

s = suma_w_potedze(5, 7, 4,4,5, 5, wart_pocz=10, wykladnik=2)
print(s)

# ---------- wyrażenie listowe
tabl = [[(i+1)*(j+1) for j in range(10)] for i in range(10)]

print(tabl)
