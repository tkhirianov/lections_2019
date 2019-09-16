# coding: utf-8
"""
Использование графического модуля graph.py.
GR_FUNC_PT - график функции по точкам
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

x0 = 150; y0 = 250; k = 50
xmin = -2; xmax = 2

windowSize(400, 400)
line(0, y0, x0+150, y0);
line(x0, 0, x0, y0+20); 
x = xmin 
h = 0.02
penColor("red")
while x <= xmax:
  y = x*x
  xe = x0 + k*x
  ye = y0 - k*y
  point(xe, ye)
  x += h 

run()