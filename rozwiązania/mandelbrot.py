from matplotlib import pyplot
N = 100                                 # --- liczba pixeli po osi X i Y

x = []
x_start = -2.5
x_stop = 1.5
x_skok = (x_stop - x_start) / float(N)  # --- krok pomiedzy punktami na osi X
for i in range(N+1):                    # --- w pętli tworzymy listę X
    x.append(x_start+x_skok*i)

y_start = -1.25
y_stop = 1.25
y_skok = (y_stop - y_start) / float(N)  # --- krok pomiedzy punktami na osi Y
y = [y_start + y_skok * i for i in range(N+1)]

# --- oblicza jeden punkt na wykresie Mandelbrota
def mandelbrot_one(x0, y0, n=100):
    x = x0
    y = y0
    for i in range(n):
        z_tmp = x*x - y*y + x0;
        y = 2.0*x*y + y0;
        x = z_tmp;
        if x*x + y*y > 4:
            return i
    return n+1

# --- tworzy kwadratową macierz z danymi do narysowania fraktala
m2d = []                                # --- macierz 2D
for i in range(N):
    wiersz = []                         # --- jeden wiersz macierzy 2D
    for j in range(N):
        w = mandelbrot_one(x[i],y[j])   # --- tu obliczamy wartości fraktala
        wiersz.append(w)                # --- ... i dodajemy do listy 1D
        # print("%d %d   %6.3f %5.2f %d" % (i, j, x[i],y[j], w))
    m2d.append(wiersz)

# --- a na koniec wykres
pyplot.imshow(m2d)
pyplot.show()