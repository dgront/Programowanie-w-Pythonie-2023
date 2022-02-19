from openpyxl import Workbook

skoroszyt = Workbook()
arkusz = skoroszyt.active
for i in range(10):
    arkusz.cell(1, i + 1, i * i)
skoroszyt.save("plik2.xlsx")


