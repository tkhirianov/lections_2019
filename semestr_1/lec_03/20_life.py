# coding: utf-8
"""
Использование графического модуля graph.py.
GR_LIFE - игра "Жизнь" Дж. Конвея
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from graph import *

cellSize = 10
fieldCellWidth = 30
fieldCellHeight = 30
fieldWidth = cellSize*fieldCellWidth
fieldHeight = cellSize*fieldCellHeight

def cellRect(y, x):
  return rectangle((x-1)*cellSize, (y-1)*cellSize,
                   x*cellSize, y*cellSize)

def initField():
  global field, fieldId
  field = [[0]*(fieldCellHeight+2) for i in range(fieldCellWidth+2)]
  fieldId = [[0]*(fieldCellHeight+2) for i in range(fieldCellWidth+2)]
  penColor("lightgray");
  brushColor("white")
  for y in range(1,fieldCellHeight+1):
    for x in range(1,fieldCellWidth+1):
       fieldId[y][x] = cellRect(y, x)

def changeField(clear = False):
  newField = [[0]*(fieldCellHeight+2) for i in range(fieldCellWidth+2)]
  if not clear:
    for y in range(1,fieldCellHeight+1):
      for x in range(1,fieldCellWidth+1):
        count = - field[y][x]
        for i in range(-1,2):
          for j in range(-1,2):
            if field[y+i][x+j]: count += 1
        if (field[y][x] == 1 and count == 2) or count == 3:
          newField[y][x] = 1
  for y in range(1,fieldCellHeight+1):
    for x in range(1,fieldCellWidth+1):
      if newField[y][x] != field[y][x]:
        toggleCell(x, y)

def toggleCell(x, y):
  field[y][x] = 1 - field[y][x]
  if field[y][x]:
    changeFillColor(fieldId[y][x], "green")
  else:
    changeFillColor(fieldId[y][x], "white")

def cellCoords(x, y):
  x = x // cellSize + 1
  y = y // cellSize + 1
  return (x, y)

prevCell = (-1,-1)
def mouseClick(event):
  global prevCell
  mouseLBMove(event)
  prevCell = (-1,-1)
  return
def mouseLBMove(event):
  global prevCell
  x, y = cellCoords(event.x, event.y)
  if (x,y) != prevCell:
    toggleCell(x, y)
    prevCell = (x, y)
  return

def update():
  global isRunning, loopCheckbox
  if isRunning:
    changeField()
    if not loopCheckbox.checked:
      goLife()

def goLife():
  global isRunning, goBtn
  isRunning = not isRunning
  if isRunning:
    goBtn["text"] = "Стоп!"
  else:
    goBtn["text"] = "Старт!"

def clearField():
  changeField(True)

def main():
  global isRunning, goBtn, isLoop, loopCheckbox
  windowSize(fieldWidth, fieldHeight+35)
  canvasSize(fieldWidth, fieldHeight)
  goBtn = button("Старт!", 7,
               fieldCellHeight*cellSize + 5, width=10,
               command = goLife )
  loopCheckbox = checkbox("Непрерывно", 80,
               fieldCellHeight*cellSize + 5 )
  clearBtn = button("Очистить", 220,
               fieldCellHeight*cellSize + 5, width=10,
               command = clearField )
  isRunning = False
  initField()
  onTimer(update, 30)
  onMouseClick(mouseClick, 1)
  onMouseButtonMove(mouseLBMove, 1)
  loopCheckbox.checked = True
  run()

main()