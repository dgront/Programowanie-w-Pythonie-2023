import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

WYS = 500
SZER = 900
TLO = (230, 240, 220)

# ---------- okno gry
oknogry = pygame.display.set_mode((SZER, WYS), 0, 32)
pygame.display.set_caption('Ping Pong')               # tytuł okna gry

# ---------- kafelki i paletka
kafelki = []
for i in range(10):
    kafelki.append((randint(0,255),randint(0,255),randint(0,255)))
pY = WYS - 50
pX = 50
pC = (255, 5, 5)        # mostly red
pspeed = 5

# pętla główna programu
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        #     pX += pspeed
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        #     pX -= pspeed
    keys = pygame.key.get_pressed()
    print(keys[pygame.K_LEFT],keys[pygame.K_RIGHT])
    if keys[pygame.K_LEFT]: pX -= pspeed
    elif keys[pygame.K_RIGHT]: pX += pspeed
    if pX <0: pX = 0
    elif pX > SZER: pX = SZER

    # rysowanie obiektów
    oknogry.fill(TLO)  # tlo rysujemy najpierw
    for i in range(len(kafelki)):
        k = kafelki[i]
        pygame.draw.rect(oknogry, k, (i*70+35, 50, 50, 20))

    pygame.draw.rect(oknogry, pC, (pX, pY, 60, 20))

    pygame.display.flip()
    # odśwież okno i wyświetl
    pygame.display.update()