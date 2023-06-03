import pygame, sys

pygame.init()

# ---------- ustawienia gry
WYS, SZER = 500, 900
KOLOR_TLA = (78, 189, 62)
KOLOR_SNK = (55, 55, 55)
SEGM_LEN = 80

# ---------- okno gry
oknogry = pygame.display.set_mode((SZER, WYS), 0, 32)
pygame.display.set_caption('wąż')               # tytuł okna gry

wonsz = [[300, 300], [300+SEGM_LEN, 300], [300+SEGM_LEN, 300-SEGM_LEN]]

def rusuj_gre():                    # --- funkcja ma rysować aktualny stan gry
    oknogry.fill(KOLOR_TLA)         # --- tlo rysujemy najpierw
    pygame.draw.rect(oknogry, KOLOR_SNK, (300, 200, 60, 10))


# ---------- pętla główna gry
while True:
    # ---------- obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ---------- odczyt klawiszy
    keys = pygame.key.get_pressed()
    # print(keys[pygame.K_LEFT])
    # ---------- logika gry
    if keys[pygame.K_LEFT]:
        print("W lewo")
    elif keys[pygame.K_RIGHT]:
        print("W prawo")

    # ---------- rysowanie gry
    rusuj_gre()                 # --- wywołaj funkcję rysującą planszę (do napisania)
    pygame.display.flip()       # --- zamień bufory
    pygame.display.update()     # --- odśwież okno i wyświetl

    pygame.time.delay(50)       # --- opóźnienie, aby sprawy nie działy się za szybko
