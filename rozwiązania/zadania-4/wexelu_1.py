from openpyxl import Workbook

skoroszyt = Workbook()
arkusz = skoroszyt.active
for i in range(10):
    arkusz.cell(row=(i+1), column=1, value=i+1)
skoroszyt.save("plik2.xlsx")


