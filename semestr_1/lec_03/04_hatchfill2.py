# coding: utf-8
"""
Использование графического модуля graph.py.
GR_HATCHFILL2 - штриховка с заливкой - 2
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

x1 = 100; y1 = 100
x2 = 300; y2 = 300
N = 10
hx = (x2 - x1) / (N + 1)
hy = (y2 - y1) / (N + 1)
hc = 255 // N
x = x1
y = y1
c = 0
for i in range(N):
  brushColor(c, 0, 0)
  polygon( [(x1,y), (x,y), (x+hx,y+hy),
            (x1,y+hy), (x1,y)] )
  x += hx
  y += hy
  c += hc

run()