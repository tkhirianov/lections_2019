# coding: utf-8
"""
Использование графического модуля graph.py.
GR_PROC - процедуры
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def treug ( x, y, c ):
  brushColor(c)
  polygon( [(x,y), (x,y-60),
            (x+100,y), (x,y)] ) 

penColor ( "black" )
treug ( 100, 100, "blue" )
treug ( 200, 100, "red" )
treug ( 200, 160, "green" )

run()