# !/usr/bin/env python3
import sys
import tkinter as tk
import tkinter.filedialog as fd

def wczytaj_plik():
    plik = fd.askopenfile()
    print(plik)
    f = open(plik.name,"r")
    txt = f.read()
    print(txt)

def exit():
    sys.exit()

okno = tk.Tk()
okno.geometry("300x200")
guzik = tk.Button(okno, text="open file", command=wczytaj_plik)
guzik.pack()
zakoncz = tk.Button(okno, text="koniec", command=exit)
zakoncz.pack()

okno.mainloop()