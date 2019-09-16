# coding: utf-8
"""
Использование графического модуля graph.py.
GR_TANK_GUN - стрельба из пушки с поворотом
         (поворот пушки - клавишами "влево" и "вправо",
          выстрел по клавише "пробел")
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *
import math

STEP = 5

def update():
  global bullet, xb, yb, isFlying, angleBullet
  if isFlying:
    if bullet == None:
      brushColor("black")
      bullet = circle(xb, yb, r)
    else:
      aRad = angleBullet*math.pi/180
      dx = STEP*math.cos(aRad)
      dy = -STEP*math.sin(aRad)
      moveObjectBy(bullet, dx, dy)
      xb += dx
      yb += dy
      if not circleInView(xb, yb, r):
        deleteObject(bullet)
        bullet = None
        isFlying = False

def keyPressed(event):
  global isFlying, bullet, xb, yb, angleBullet
  if event.keycode == VK_LEFT:
    drawGun(angle+5)
  elif event.keycode == VK_RIGHT:
    drawGun(angle-5)
  elif event.keycode == VK_SPACE:
    if not isFlying:
      angleBullet = angle
      aRad = angle*math.pi/180
      xb = x0+L*math.cos(aRad)
      yb = y0-L*math.sin(aRad)
      isFlying = True
  elif event.keycode == VK_ESCAPE:
    close()

def drawGun(angleNew):
  global angle, gun
  angle = angleNew
  aRad = angle*math.pi/180
  x1 = x0+L*math.cos(aRad)
  y1 = y0-L*math.sin(aRad)
  if gun == None:
    gun = line(x0, y0, x1, y1)
  else:
    changeCoords(gun, [(x0,y0), (x1,y1)] )

H = 60; W = 30; L = 40
x0 = 200; y0 = 400; angle = 90
r = 3
gun = None
xb = x0; yb = x0
isFlying = False
bullet = None
brushColor("#6b8e23")
rectangle(x0-W/2, y0-H/2, x0+W/2, y0+H/2)
penSize(5)
drawGun(angle)
penSize(1)
brushColor("#556b2f")
circle(x0, y0, W/2)

onKey(keyPressed)
onTimer(update, 30)

run()