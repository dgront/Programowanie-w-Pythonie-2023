from math import sin, cos
from matplotlib import pyplot

N = 140
krok = 0.1
t = 0
R = 100
r = 15
h = 10

for n in range(0,100,10):
    daneX = []
    daneY = []
    for i in range(n):
        t = t + krok
        x = (R+r) * cos(t) - h * cos((R+r)/r * t)
        y = (R+r) * sin(t) - h * sin((R+r)/r * t)
        daneX.append(x)
        daneY.append(y)
    pyplot.axes().set_aspect('equal')
    pyplot.xlim(-130, 130)
    pyplot.ylim(-130, 130)
    pyplot.plot(daneX, daneY)
    pyplot.show()