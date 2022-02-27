import copy

N = 5
# --- listy możemy inicjować od razu z ich zawartością
l1 = [1, 2, 3]
l2 = [5, 6, 7, 8, 9]
l3 = [8, 2, 4]

# --- lista dwuwymiarowa to po prostu lista list
ll = [l1, l2, l3]

# --- Drukownie listy 2D wyświetla na ekranie wewnętrzne listy
# ----------------- wariant 0
for i in range(len(ll)):
    print(ll[i])

# ----------------- wariant 1
for i in range(len(ll)):
    jakas_l = ll[i]
    print(jakas_l)

# ----------------- wariant 2
for li in ll:
    print(li)

# --- Drukownie wartości z listy 2D wymaga podwójnie zagnieżdżonej pętli
# ----------------- wariant 1
for i in range(len(ll)):
    jakas_l = ll[i]
    for j in range(len(jakas_l)):
        print(jakas_l[j], end=" ")
    print()

# ----------------- wariant 2
for i_lista in ll:
    for wart in i_lista:
        print(wart, end=" ")
    print()

# ----- kopie płytkie i głębokie
l_stara = [1, 2, 3]
l_nowa = l_stara            # --- kopia płytka
l_nowa_naprawde = []        # --- kopia głęboka
for val in l2:
    l_nowa_naprawde.append(val)

l2.append("NIESPODZIANKA")

print(l_stara, l_nowa, l_nowa_naprawde)







