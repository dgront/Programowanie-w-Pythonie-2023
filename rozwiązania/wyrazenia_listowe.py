# ---------------- Garść przykładów z wyrażeniami listowymi
z = [0 for i in range(10)]              # --- najprostsze: wstaw 10 zer do listy
z = [i for i in range(10)]              # --- wstaw 10 kolejnych liczb do listy
z = [i*i for i in range(10)]            # --- wstaw kwadraty 10 kolejnych liczb

# --- przykład z zadania o fraktalu: generowanie listy równoodległych punktów
y_start = -2.0
y_skok = 0.25
N = 10
y = [y_start + y_start * i for i in range(N+1)]