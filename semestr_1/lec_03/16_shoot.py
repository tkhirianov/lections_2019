# coding: utf-8
"""
Использование графического модуля graph.py.
GR_SHOOT - полет снаряда
         (старт по клавише "пробел")
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def update():
  global isFlying, bullet
  if isFlying:
    y = coords(bullet)[1]
    if y < r:
      moveObjectTo(bullet, x0-r, y0-r)
      isFlying = False
    else:
      moveObjectBy(bullet, 0, -5)

def keyPressed(event):
  global isFlying
  if event.keycode == VK_SPACE:
    isFlying = True
  elif event.keycode == VK_ESCAPE:
    close()

x0 = 200; y0 = 400; r = 3
isFlying = False
brushColor("black")
bullet = circle(x0, y0, r)
onKey(keyPressed)
onTimer(update, 30)
run()
