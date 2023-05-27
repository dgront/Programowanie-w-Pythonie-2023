import pygame, sys

pygame.init()

# ---------- ustawienia gry
WYS, SZER = 500, 900
KOLOR_TLA = (230, 240, 220)
KOLOR_SNK = (5, 5, 5)

# ---------- okno gry
oknogry = pygame.display.set_mode((SZER, WYS), 0, 32)
pygame.display.set_caption('wąż')               # tytuł okna gry

def rusuj_gre():
    """ rysowanie obiektów"""
    oknogry.fill(KOLOR_TLA)  # ---------- tlo rysujemy najpierw
    pygame.draw.rect(oknogry, KOLOR_SNK, (300, 300, 60, 10))


# pętla główna gry
while True:
    # obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rusuj_gre()
    pygame.display.flip()
    # odśwież okno i wyświetl
    pygame.display.update()