# coding: utf-8
"""
Использование графического модуля graph.py.
GR_PLATES - стрельба по тарелочкам
         (выстрел по клавише "пробел")
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *
from random import randint

def createPlates( N ):
  global plates
  yPlates = 100
  plates = []
  for i in range(N):
    brushColor( randColor() )
    p = circle(randint(0,500), yPlates, randint(10,20))
    plates.append(p)

def hit(p):
  global bullet
  x1,y1,x2,y2 = coords(bullet)
  xb = x1 + r; yb = y1 + r
  x1p, y1p, x2p, y2p = coords(p)
  xp = (x1p + x2p) / 2
  yp = (y1p + y2p) / 2
  Rp = (x2p - x1p) / 2
  d2 = (xb-xp)**2 + (yb-yp)**2
  return d2 <= (r+Rp)**2

def movePlates():
  global plates
  for p in plates:
    moveObjectBy(p, -2, 0)
    x1, y1, x2, y2 = coords(p)
    if x1 < 0:
      moveObjectBy(p, randint(500,600), 0)

def checkCollision():
  global isFlying, bullet, plates, lbl, score
  for p in plates:
    if hit(p):
      moveObjectBy(p, randint(500,600), 0)
      score += 1
      lbl["text"] = "Счёт: " + str(score)
      moveObjectTo(bullet, x0-r, y0-r)
      isFlying = False
      break

def update():
  global isFlying, bullet
  movePlates()
  if isFlying:
    y = coords(bullet)[1]
    if y < 0:
      moveObjectTo(bullet, x0-r, y0-r)
      isFlying = False
    else:
      moveObjectBy(bullet, 0, -10)
      checkCollision()

def keyPressed(event):
  global isFlying
  if event.keycode == VK_SPACE:
    isFlying = True
  elif event.keycode == VK_ESCAPE:
    close()

x0 = 200; y0 = 400; r = 3

createPlates( 5 )

brushColor("black")
bullet = circle(x0, y0, r)
isFlying = False

score = 0
lbl = label("Счёт: 0", 10, 200, bg = "white")

onKey(keyPressed)
onTimer(update, 10)

run()