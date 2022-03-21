# !/usr/bin/env python3
import tkinter as tk
import tkinter.filedialog as fd
# from tkinter import *

# ------ Wyrażenie budowane przez klikanie na kalkulatorze
wyrazenie = ""

# ------ Funkcja wywoływana po każdym kliknięciu na jakikolwiek guzik
def dopisz(evt=None):
    global wyrazenie, dopisywanie, result

    guzik = evt.widget
    print(guzik["text"], str(guzik))
    if guzik["text"] == "AC":
        wyrazenie = ""
        result.config(text="0.0")
        expr_label.config(text="0.0")
    elif guzik["text"] == "=":
        wynik = eval(wyrazenie)
        wyrazenie = ""
        result.config(text=str(wynik))
        print(wynik)
    else:
        wyrazenie += dopisywanie[str(guzik)]
        expr_label.config(text=wyrazenie)
        print(wyrazenie)

okno = tk.Tk()
okno.title("Kalkulator")
okno.geometry("500x350")

guziki_txt = ["(", ")", "%", "AC", "7", "8", "9", "/", "4"
    , "5", "6", "-", "1", "2", "3", "+", "0", ",", "*", "="]

guziki_obj = {}
dopisywanie = {}
i = 0
result = tk.Label(okno,height=1, width=10, text="0.0")
result.place(x=20,y=10)
expr_label = tk.Label(okno,height=1, width=10, text="0.0")
expr_label.place(x=20,y=50)

for nazwa in guziki_txt:
    guzik = tk.Button(okno, text=nazwa, name="g"+nazwa,
                      width=8, height=2)
    guzik.bind("<Button>",dopisz)
    guzik.place(x=20 + (i%4)*100, y=70+(i//4)*50)
    dopisywanie[str(guzik)] = nazwa
    # print(guzik)
    i += 1

okno.mainloop()
