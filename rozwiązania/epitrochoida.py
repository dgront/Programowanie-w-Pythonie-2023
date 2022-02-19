from math import sin, cos
from matplotlib import pyplot

N = 1000        # Liczba punktów na wykresie
krok = 0.1      # jak często punkty?
R = 100         # promień dużego koła
r = 15          # promień małego koła
h = 10          # położenie punktu

t = 0
daneX = []      # lista na wyniki - wsp X
daneY = []      # lista na wyniki - wsp Y
for i in range(N):
    t = t + krok
    x = (R+r) * cos(t) - h * cos((R+r)/r * t)
    y = (R+r) * sin(t) - h * sin((R+r)/r * t)
    daneX.append(x)
    daneY.append(y)
pyplot.axes().set_aspect('equal')   # niech wykres będzie kwadratowy
pyplot.xlim(-130, 130)              # zakresy osi x
pyplot.ylim(-130, 130)              # zakresy osi y
pyplot.plot(daneX, daneY)           # wykres liniowy
pyplot.show()                       # pokaż wykres