from openpyxl import Workbook
from openpyxl.styles.colors import Color
from openpyxl.styles import PatternFill
from colormap import rgb2hex

N = 20

w = Workbook()
arkusz = w.active
for row in range(N):
    red = int(255 / N * row)
    for col in range(N):
        blue = int(255 / N * col)
        color_as_str = rgb2hex(red, 100, blue)
        arkusz.cell(row+1, col+1, 5)
        komorka = arkusz.cell(row+1, col+1)
        color = Color(color_as_str[1:], type='rgb')
        komorka.fill = PatternFill(patternType='solid',fill_type='solid', fgColor=color)
w.save("plik2.xlsx")
