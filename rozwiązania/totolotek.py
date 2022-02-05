import random

N = 10000  # Tyle "kuponów" losujemy
K = 49  # liczba kul
# ------ trzeba zainicjalizować tablicę tak, aby miała 49 zer
T = [0 for i in range(K + 1)]

for j in range(N):  # --- pętla po losowaniach
    for i in range(6):  # --- 6 kul w każdym losowaniu
        kula = int(random.random() * K) + 1
        # ---------- Tu zliczamy krotność kul
        T[kula] = T[kula] + 1

print("statystyki:")
for i in range(len(T)):
    print("ile razy", i, ":", T[i])