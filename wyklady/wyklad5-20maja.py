# ---------- slice czyli wycinek listy lub napisu

s = "FPVPKGVLRIHFIEAQDLQGKDTYLKGLVKGKSDPYGIIRVGNQIFQSRVIKENLSPKWNEVYEALVYEHPGQELEIELFDEDPDKDDFLGSLMIDLIEVEKERLLDEWFTLDEVPKGKLHLRLEWLTLMPNVSNLDKVLTDIKADGLSSALLILYLDSARNLPSSNPNPVVQMSVGHKAQESKIRYKTNEPVWEENFTFFIHNPKRQDLEVEVRDEQHQCSLGNLKVPLSQLLTSEDMTVSQRFQLSNSGPNSTIKMKIALRVLHLEK"
N = 5
i = 8
# plasterek = s[i:i + N + 1]

# ---------- Wczytywanie CSV w pandas
import pandas as pd
df = pd.read_csv("../dane/pokemon.csv", sep=',')
# --- drukowanie nazw kolumn
for col_name in df:
    print(col_name)

# --- dostęp do wierszy
mw = df.loc[:, ["height_m","weight_kg"]]

# import matplotlib.pyplot as plt
# plt.scatter(wzrost, masa)
# plt.show()
# x = df.loc[df.type1=="bug",["name","against_water", "type1"]]
print(mw.sort_values(by="weight_kg"))

x = df.loc[0, :]
print(x)
# --- dostęp do kolumny
wzrost = df.loc[:, "height_m"]
masa = df.loc[:, "weight_kg"]
bmi = masa / (wzrost*wzrost)
print(bmi.sort_values())
print("iloraz dla p0",6.9/(0.7*0.7))

typy = df.loc[df.type1=="rock", "against_bug"]
print(typy.mean())

# --- dostęp do wielu kolumn
masa_nazwa = df.loc[:, ["weight_kg", "name"]]
# wynik = masa_nazwa.sort_values(by="weight_kg")
# print(wynik)

# --- dostęp do pól
x = df.iloc[8, 8]
# print(x)
x = df.loc[8, ["name", "hp", "generation"]]
x = df.loc[0, "name"]
x = df.loc[0, ["name"]]
# print(x)

suma_po_genie = df.loc[:, ["generation"]].pivot_table(index = ['generation'], aggfunc ='size')
print(suma_po_genie)
suma_po_trybie = df.loc[:, ["type1"]].pivot_table(index = ['type1'], aggfunc ='size')
print(suma_po_trybie)
print(df.loc[lambda e: (e.type1=="flying") | (e.type2=="flying"), ["name"]])