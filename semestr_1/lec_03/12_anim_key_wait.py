# coding: utf-8
"""
Использование графического модуля graph.py.
GR_ANIM_KEY_WAIT - анимация с управлением клавишами-стрелками
         (с ожиданием нажатия на клавишу)
  (C) К. Поляков, 2017-2018
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def keyPressed(event):
  if event.keycode == VK_LEFT:
    moveObjectBy(obj, -5, 0)
  elif event.keycode == VK_RIGHT:
    moveObjectBy(obj, 5, 0)
  elif event.keycode == VK_UP:
    moveObjectBy(obj, 0, -5)
  elif event.keycode == VK_DOWN:
    moveObjectBy(obj, 0, 5)
  elif event.keycode == VK_ESCAPE:
    close()

brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)
onKey(keyPressed)

run()