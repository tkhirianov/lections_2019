# coding: utf-8
"""
Использование графического модуля graph.py.
CATCH_BALL - поймай шарик щелчком по нему
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *
from random import randint
from math import sin, cos, pi

balls = []
score = 0
step = 1
Rmin = 10
Rmax = 20
fieldWidth = 300
fieldHeight = 400

def createBalls( N ):
  global balls
  for i in range(N):
    brushColor( randColor() )
    R = randint(Rmin, Rmax)
    angle = randint(0,360)
    xc = randint(R,fieldWidth-R)
    yc = randint(R,fieldHeight-R)
    id = circle(xc, yc, R)
    balls.append( [id, xc, yc, R, angle] )

def moveBalls():
  global balls
  for i in range(len(balls)):
    id, xc, yc, R, angle = balls[i]
    dx = step*cos(angle*pi/180)
    dy = step*sin(angle*pi/180)
    xc += dx
    yc -= dy
    balls[i][1] = xc
    balls[i][2] = yc
    moveObjectBy(id, dx, -dy)
    if xc < R or xc+R > fieldWidth:
      angle = 180 - angle
    elif yc < R or yc+R > fieldHeight:
      angle = 360 - angle
    balls[i][4] = angle

def hit(b, x, y):
  id, xc, yc, R, _ = b
  d2 = (x-xc)**2 + (y-yc)**2
  return d2 <= R**2

def mouseCLick(event):
  global lbl, score, balls
  for b in balls:
    if hit(b, event.x, event.y):
       score += Rmax + 1 - b[3]
       lbl["text"] = "Счёт: " + str(score)
       deleteObject(b[0])
       balls.remove(b)
       createBalls(1)
       break

def update():
  moveBalls()

def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()

def main():
  global lbl
  canvasPos(0, 25)
  canvasSize(fieldWidth, fieldHeight)
  windowSize(fieldWidth+2, fieldHeight+27)
  createBalls( 10 )
  lbl = label("Счёт: 0", 10, 0, font="Arial, 12")
  onKey(keyPressed)
  onMouseClick(mouseCLick)
  onTimer(update, 10)
  run()

main()