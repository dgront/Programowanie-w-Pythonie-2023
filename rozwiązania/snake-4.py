import pygame, sys, random

pygame.init()

# ---------- ustawienia gry
WYS, SZER = 500, 900
KOLOR_TLA = (78, 189, 62)
KOLOR_SNK = (55, 55, 55)
SEGM_LEN = 50
SEGM_SZR = 10

# ---------- okno gry
oknogry = pygame.display.set_mode((SZER, WYS), 0, 32)
pygame.display.set_caption('wąż')               # tytuł okna gry

wonsz = [[300, 300], [300+SEGM_LEN, 300], [300+SEGM_LEN, 300-SEGM_LEN]]
kropki = []


def rysuj_gre():                    # --- funkcja ma rysować aktualny stan gry
    oknogry.fill(KOLOR_TLA)         # --- tlo rysujemy najpierw
    pygame.draw.lines(oknogry, KOLOR_SNK, False, wonsz, width=SEGM_SZR)
    for x, y in wonsz:
        pygame.draw.circle(oknogry, KOLOR_SNK, (x+1, y+1), SEGM_SZR/2)
    # --- a teraz rysujemy kropki
    for x, y in kropki:
        pygame.draw.circle(oknogry, KOLOR_SNK, (x+1, y+1), SEGM_SZR/2)


def rysuj_game_over():
    oknogry.fill(KOLOR_TLA)         # --- tlo rysujemy najpierw
    font = pygame.font.SysFont('arial', 40)
    txt = font.render('Game Over', True, KOLOR_SNK)
    oknogry.blit(txt, (100, 100))

def przesun_weza(dx, dy):
    wonsz.pop(0)
    nowy_x = wonsz[-1][0] + dx
    nowy_y = wonsz[-1][1] + dy
    wonsz.append([nowy_x, nowy_y])


def dodaj_kropke(prob, max_kropek):
    los = random.random()
    if los < prob and len(kropki) < max_kropek:
        nx = int(SZER / SEGM_LEN) - 2
        ny = int(WYS / SEGM_LEN) - 2
        x = random.randint(1, nx) * SEGM_LEN
        y = random.randint(1, ny) * SEGM_LEN
        kropki.append((x, y))


def zjedz_kropke():
    px, py = wonsz[-1]
    i_kropki = 0
    for x, y in kropki:
        if x==px and y == py:
            kropki.pop(i_kropki)
            ppx, ppy = wonsz[-2]
            wonsz.append([px+px-ppx, py+py-ppy])
        i_kropki += 1


def czy_kolizja():
    px, py = wonsz[-1]              # --- rozpakujmy współrzędne końca węża
    for ix, iy in wonsz[0:-2]:      # --- pętla po reszcie węża, bez głowy
        if ix == px and iy == py:
            return True
    return False

# ---------- pętla główna gry
while True:
    # ---------- obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ---------- odczyt klawiszy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit(0)
    # print(keys[pygame.K_LEFT])
    # ---------- logika gry
    if keys[pygame.K_LEFT]:
        przesun_weza(-SEGM_LEN, 0)
    elif keys[pygame.K_RIGHT]:
        przesun_weza(SEGM_LEN, 0)
    elif keys[pygame.K_UP]:
        przesun_weza(0, -SEGM_LEN)
    elif keys[pygame.K_DOWN]:
        przesun_weza(0, SEGM_LEN)

    dodaj_kropke(0.1, 5)
    zjedz_kropke()

    # ---------- rysowanie gry
    if czy_kolizja():
        rysuj_game_over()           # --- koniec gry
    else:
        rysuj_gre()                 # --- wywołaj funkcję rysującą planszę

    pygame.display.flip()       # --- zamień bufory
    pygame.display.update()     # --- odśwież okno i wyświetl

    pygame.time.delay(50)       # --- opóźnienie, aby sprawy nie działy się za szybko
