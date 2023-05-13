from openpyxl import Workbook

skoroszyt = Workbook()
arkusz = skoroszyt.active
for i in range(1,11):
    for j in range(1,11):
        arkusz.cell(row=i, column=j, value=i*j)
skoroszyt.save("plik2.xlsx")


