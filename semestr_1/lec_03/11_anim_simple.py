# coding: utf-8
"""
Использование графического модуля graph.py.
GR_ANIM_SIMPLE - простая анимация
  (C) К. Поляков, 2017-2018
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def update():
  moveObjectBy(obj, 5, 0)
  if xCoord(obj) >= 400-20: close()
def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()

brushColor("blue")
rectangle(0, 0, 400, 400)
x = 100
y = 100
penColor("yellow")
brushColor("yellow")
obj = rectangle(x, y, x+20, y+20)

onKey(keyPressed)
onTimer(update, 50)

run()