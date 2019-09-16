# coding: utf-8
"""
Использование графического модуля graph.py.
GR_TANK_ROTATE - танк с вращающейся башней
         (используйте клавиши "влево"-"вправо")
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *
import math

def keyPressed(event):
  if event.keycode == VK_LEFT:
    drawGun(angle+5)
  elif event.keycode == VK_RIGHT:
    drawGun(angle-5)
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
gun = None
brushColor("#6b8e23")
rectangle(x0-W/2, y0-H/2, x0+W/2, y0+H/2)
penSize(5)
drawGun(angle)
penSize(1)
brushColor("#556b2f")
circle(x0, y0, W/2)

onKey(keyPressed)

run()