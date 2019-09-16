# coding: utf-8
"""
Использование графического модуля graph.py.
GR_ANIM_SNAKE - анимация змейки с управлением 
         клавишами-стрелками ("по требованию", при 
         нажатии клавиш-стрелок меняется направление 
         движения)
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

def moveSnake(xNew, yNew):
  global x, y
  for k in range(len(snake)-1,0,-1):
    newCoord = coords(snake[k-1])
    moveObjectTo(snake[k], newCoord[0], newCoord[1])
  moveObjectTo(snake[0], xNew, yNew)
  x = xNew
  y = yNew

def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT: 
    dx = -1; dy = 0 
  elif event.keycode == VK_RIGHT:
    dx = 1; dy = 0 
  elif event.keycode == VK_UP:
    dx = 0; dy = -1 
  elif event.keycode == VK_DOWN:
    dx = 0; dy = 1 
  elif event.keycode == VK_SPACE:
    dx = dy = 0
  elif event.keycode == VK_ESCAPE:
    close() 

def doMove():
  global dx, dy
  if dx or dy:
    xNew = x + dx*a
    yNew = y + dy*a
    if xNew < 0: 
      dx = 0 
      if yNew > 0: dy = -1
      else: dy = 1
    elif yNew < 0:
      dy = 0
      if xNew > 0: dx = -1
      else: dx = 1
    elif xNew > 400-a:
      dx = 0
      if yNew < 400-a: dy = 1
      else: dy = -1
    elif yNew > 400-a:  
      dy = 0
      if xNew < 400-a: dx = 1
      else: dx = -1
    else: moveSnake(xNew, yNew)
 
brushColor("blue")
rectangle(0, 0, 400, 400)

x = 100; y = 100
dx = 0;  dy = 0
a = 10; N = 20

snake = []
penColor("yellow")
brushColor("yellow")
for i in range(0,N):
  snake.append( rectangle(x+i*a, y, x+i*a+a, y+a) )
  brushColor("green")

onKey(keyPressed)
onTimer(doMove, 50)

run()