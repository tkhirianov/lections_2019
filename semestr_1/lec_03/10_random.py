# coding: utf-8
"""
Использование графического модуля graph.py.
GR_RANDOM - прямоугольник заполняется точками
            случайного цвета, выход по Escape            
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *
from random import randint, choice

colors = ["red", "green", "blue", "black", "#FFFF00"]
def newPoint():
  x = randint(0, 150)
  y = randint(0, 150)
  if randint(0,1) == 0:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    penColor(r, g, b)
  else:  
    col = choice(colors)
    penColor( col )
  point(x, y)
 
def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()   

onKey(keyPressed)
onTimer(newPoint, 10)

run()