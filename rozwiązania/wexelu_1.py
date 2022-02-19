from openpyxl import Workbook

w = Workbook()
arkusz = w.active
for i in range(10):
    arkusz.cell(1, i + 1, i * i)
w.save("plik2.xlsx")


