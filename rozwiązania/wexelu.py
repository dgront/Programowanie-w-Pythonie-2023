import sys
from math import *
from random import random as rnd
from random import randint as rni

from openpyxl import Workbook

w = Workbook()
arkusz = w.active
w.save("plik2.xlsx")


