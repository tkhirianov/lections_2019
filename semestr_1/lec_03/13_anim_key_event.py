# coding: utf-8
"""
Использование графического модуля graph.py.
GR_ANIM_KEY_EVENT - анимация с управлением клавишами-стрелками
         ("по требованию", при нажатии клавиш-стрелок
          меняется направление движения)
  (C) К. Поляков, 2017-2018
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT:
    dx = -5; dy = 0
  elif event.keycode == VK_RIGHT:
    dx = 5; dy = 0
  elif event.keycode == VK_UP:
    dx = 0; dy = -5
  elif event.keycode == VK_DOWN:
    dx = 0; dy = 5
  elif event.keycode == VK_SPACE:
    dx = dy = 0
  elif event.keycode == VK_ESCAPE:
    close()
def update():
  moveObjectBy(obj, dx, dy)

brushColor("blue")
rectangle(0, 0, 400, 400)

x = 100; y = 100
dx = 0;  dy = 0
penColor("yellow")
brushColor("yellow")
#obj = rectangle(x, y, x+20, y+20)
obj = circle(x, y, 20)

onKey(keyPressed)
onTimer(update, 50)

run()