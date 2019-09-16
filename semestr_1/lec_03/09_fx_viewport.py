# coding: utf-8
"""
Использование графического модуля graph.py.
GR_FX_VIEWPORT - построение графика в преобразованной системе координат
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def f(x):
    return x**3

viewCoords(-1, 1,  # пределы по оси X
           -1, 1)  # пределы по оси Y

line(-1, 0, 1, 0)  # ось X
line(0, -1, 0, 1)  # ось Y

x = -1             # начальная точка
moveTo ( x, f(x) )
while x <= 1:
    y = lineTo ( x, f(x) )
    x += 0.1

  # метки на осях
label("X", 0.8, -0.1 )
label("Y", 0.1, 0.8 )
label("График функции y = x^3", -0.6, -0.5)

run()