# -*- coding: utf-8 -*-
"""
GRAPH - модуль для простой графики в Python.
  (C) К. Поляков, 2017-2018
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
  Версия 1.4.1

Модуль graph - это "обертка" над стандартной библиотекой tkinter,
позволяющая рисовать простыми командами в отдельном графическом окне.
В ней упрощён доступ ко многим возможностям библиотеки tkinter,
в то же время сохранена возможность использования всех средств tkinter.

ЛИЦЕНЗИЯ

Copyright (c) 2016-2018, Константин Поляков
Все права защищены.

Разрешается повторное распространение и использование как в виде исходного
кода, так и в двоичной форме, с изменениями или без, при соблюдении
следующих условий:
  1) При повторном распространении исходного кода должно оставаться указанное
     выше уведомление об авторском праве, этот список условий и последующий
     отказ от гарантий.
  2) При повторном распространении двоичного кода должна сохраняться указанная
     выше информация об авторском праве, этот список условий и последующий
     отказ от гарантий в документации и/или в других материалах,
     поставляемых при распространении.
  3) Ни название Организации, ни имена ее сотрудников не могут быть
     использованы в качестве поддержки или продвижения продуктов,
     основанных на этом ПО без предварительного письменного разрешения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ ЛЮБОГО ВИДА
ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ
ГАРАНТИЯМИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ
И НЕНАРУШЕНИЯ ПРАВ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ
ОТВЕТСТВЕННОСТИ ПО ИСКАМ О ВОЗМЕЩЕНИИ УЩЕРБА, УБЫТКОВ ИЛИ ДРУГИХ ТРЕБОВАНИЙ
ПО ДЕЙСТВУЮЩИМ КОНТРАКТАМ, ДЕЛИКТАМ ИЛИ ИНОМУ, ВОЗНИКШИМ ИЗ, ИМЕЮЩИМ ПРИЧИНОЙ
ИЛИ СВЯЗАННЫМ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ПРОГРАММНОГО
ОБЕСПЕЧЕНИЯ ИЛИ ИНЫМИ ДЕЙСТВИЯМИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.
"""

"""
Исходя из http://docs.python.org/3/library/sys.html внесены исправления для
обеспечения работоспособности в ОС Linux (С. Целищев).
"""
from sys import platform

if platform == "win32" or platform == "cygwin":
        VK_SPACE  = 0x20
        VK_PRIOR  = 0x21 # PAGE UP key
        VK_NEXT   = 0x22 # PAGE DOWN key
        VK_END    = 0x23 # END key
        VK_HOME   = 0x24 # HOME key
        VK_LEFT   = 0x25
        VK_UP     = 0x26
        VK_RIGHT  = 0x27
        VK_DOWN   = 0x28
        VK_INSERT = 0x2D # INS key
        VK_DELETE = 0x2E # DELETE key
        VK_BACK   = 0x08 # BACKSPACE key
        VK_TAB    = 0x09 # TAB key
        VK_RETURN = 0x0D # RETURN key
        VK_ESCAPE = 0x1B # ESC key
elif platform == "linux":
        VK_SPACE  = 0x41
        VK_PRIOR  = 0x70 # PAGE UP key
        VK_NEXT   = 0x75 # PAGE DOWN key
        VK_END    = 0x73 # END key
        VK_HOME   = 0x6E # HOME key
        VK_LEFT   = 0x71
        VK_UP     = 0x6F
        VK_RIGHT  = 0x72
        VK_DOWN   = 0x74
        VK_INSERT = 0x76 # INS key
        VK_DELETE = 0x77 # DELETE key
        VK_BACK   = 0x16 # BACKSPACE key
        VK_TAB    = 0x17 # TAB key
        VK_RETURN = 0x24 # RETURN key
        VK_ESCAPE = 0x09 # ESC key

DEF_GRAPH_WIDTH = 500
DEF_GRAPH_HEIGHT = 600

import tkinter
from random import randint
try:
  from PIL import ImageTk, Image
except:
  pass

NW = tkinter.NW
N = tkinter.N
NE = tkinter.NE
W = tkinter.W
CENTER = tkinter.CENTER
E = tkinter.E
SW = tkinter.SW
S = tkinter.S
SE = tkinter.SE

#----------------------------------
class onTimerCall():
  def __init__(self, _func, _timeInterval):
    self.func = _func
    self.timeInterval = _timeInterval
    self.active = True
#----------------------------------
def __initGraph__():
  global _win, _C, _Cw, _Ch, _Cpos
  global _pos, _penColor, _brushColor, _penSize
  global _timerCalls, _viewPort
  global _images
  _win = tkinter.Tk()
  _win.configure(bg="white")
  _win.geometry(str(DEF_GRAPH_WIDTH)+"x"+
                str(DEF_GRAPH_HEIGHT)+"+100+100")
  _viewPort = None
  _Cw = DEF_GRAPH_WIDTH
  _Ch = DEF_GRAPH_HEIGHT
  _C = tkinter.Canvas(_win, background='white', bd=0, highlightthickness=1,
                      width=_Cw, height=_Ch)
  _Cpos = [0, 0]
  _C.place(x = _Cpos[0], y = _Cpos[1])
  _penColor = "black"
  _penSize = 1
  _brushColor = ""
  _pos = (0,0)
  _timerCalls = []
  _images = []
#----------------------------------
def mainWindow():
  return _win
def canvas():
  return _C
#----------------------------------
def canvasPos(x = -1, y = -1):
    global _C, _Cpos
    if x >= 0:
      _C.place(x = x, y = y)
      _Cpos = [x, y]
    else:
      return tuple(_Cpos)
#----------------------------------
def canvasSize(w = -1, h = -1):
    global _C, _Cw, _Ch
    if w > 0:
      _C.config(width = w, height = h)
      _Cw = w
      _Ch = h
    else:
      return (_Cw, _Ch)
#----------------------------------
def pointInView(x, y):
  w, h = windowSize()
  return (x > 0 and y > 0 and x < h and y < h)
def circleInView(x, y, r):
  w, h = windowSize()
  return (x > r and y > r and x < w-r and y < h-r)
#----------------------------------
def windowSize(w = -1, h = -1):
  global _win
  _win.update()
  geom = _win.geometry().split("+")
  if w != -1:
    _win.geometry( "%dx%d+%s+%s" % (w, h, geom[1], geom[2]) )
  else:
    w, h = map(int, geom[0].split("x"))
    return (w, h)
#----------------------------------
def viewCoords(x1 = None, x2 = -1, y1 = -1, y2 = -1):
  global _viewPort
  if ~(x1 is None):
    _viewPort = (x1, x2, y1, y2)
  else:
    geom = windowSize()
    _viewPort = None
#----------------------------------
def penColor(c = -1, g = -1, b = -1):
  global _penColor
  if type(c) == tuple: c, g, b = c
  if c != -1:
    if g != -1:
      c = "#%02X%02X%02X" % (c, g, b)
    _penColor = c
  else:
    return _penColor
#----------------------------------
def penSize(c = -1):
  global _penSize
  if c != -1:
    _penSize = c
  else:
    return _penSize
#----------------------------------
def brushColor(c = -1, g = -1, b = -1):
  global _brushColor
  if type(c) == tuple: c, g, b = c
  if c != -1 :
    if c != "":
      if g != -1:
        c = "#%02X%02X%02X" % (c, g, b)
    _brushColor = c
  else:
    return _brushColor
#----------------------------------
def randColor():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  col = "#%02X%02X%02X" % (r, g, b)
  return col
#----------------------------------
def transformCoord(x, y):
  global _viewPort
  if _viewPort:
    x1, x2, y1, y2 = _viewPort
    w, h = windowSize()
    x = (x - x1)*w/(x2 - x1)
    y = (y2 - y)*h/(y2 - y1)
  return x, y
#----------------------------------
def moveTo(x, y = -1):
  global _pos
  if type(x) == tuple: x, y = x
  x, y = transformCoord(x, y)
  _pos = (x, y)
#----------------------------------
def lineTo(x, y = -1):
  global _pos
  if type(x) == tuple: x, y = x
  x, y = transformCoord ( x, y )
  line = _C.create_line(_pos[0], _pos[1], x, y,
                 fill = _penColor,
                 width = _penSize )
  _pos = (x, y)
  return line
#----------------------------------
def point(x, y, col = -1):
  old_col = penColor()
  if col != -1: penColor(col)
  moveTo(x, y)
  pt = lineTo(x+1,y)
  penColor(old_col)
  return pt
#----------------------------------
def line(x1, y1, x2, y2):
  x1, y1 = transformCoord ( x1, y1 )
  x2, y2 = transformCoord ( x2, y2 )
  line = _C.create_line(x1, y1, x2, y2,
                 fill = _penColor,
                 width = _penSize)
  return line
#----------------------------------
def unpackCoord(points):
  coord = []
  for p in points:
    x, y = transformCoord(p[0], p[1])
    coord.extend( (x, y) )
  return coord
#----------------------------------
def polyline(points):
  coord = unpackCoord(points)
  line = _C.create_line(*coord,
                 fill = _penColor,
                 width = _penSize)
  return line
#----------------------------------
def rectangle(x1, y1, x2, y2):
  x1, y1 = transformCoord ( x1, y1 )
  x2, y2 = transformCoord ( x2, y2 )
  rect = _C.create_rectangle(x1, y1, x2, y2,
                      outline = _penColor,
                      width = _penSize,
                      fill = _brushColor)
  return rect
#----------------------------------
def circle(x, y, R):
  x1 = x - R; y1 = y - R
  x2 = x + R; y2 = y + R
  x1, y1 = transformCoord ( x1, y1 )
  x2, y2 = transformCoord ( x2, y2 )
  circ = _C.create_oval(x1, y1, x2, y2,
                 outline = _penColor,
                 width = _penSize,
                 fill = _brushColor)
  return circ
#----------------------------------
def polygon(points):
  coord = unpackCoord(points)
  if points[0] != points[-1]:
     points.append( points[0] )
  plg = _C.create_polygon(*coord,
        outline=_penColor, width = _penSize,
        fill=_brushColor)
  return plg
#----------------------------------
def image(x, y, fileName, anchor = NW, **kwargs):
  if type(x) == tuple:
    fileName = y
    x, y = x
  x, y = transformCoord ( x, y )
  try:
   if fileName.lower().endswith('.gif'):
     newImage = tkinter.PhotoImage(file = fileName)
   else:
     im = Image.open(fileName)
     newImage = ImageTk.PhotoImage(im)
  except:
   pass
  _images.append(newImage)
  img = _C.create_image(x, y, image = newImage, anchor = anchor, **kwargs)
  return img
#----------------------------------
def label(_text, _x, _y, **kwargs):
  kwargs["bg"] = kwargs.get("bg", "white")
  lbl = tkinter.Label(_win, text = _text,  **kwargs)
  _x, _y = transformCoord(_x, _y)
  lbl.place(x = _x, y = _y)
  return lbl
#----------------------------------
def checkbox(_text, _x, _y, **kwargs):
  def _setChecked(self, value):
    self.var.set(value)
    print('set', value)
  kwargs["bg"] = kwargs.get("bg", "white")
  cbx = tkinter.Checkbutton( _win, text = _text, **kwargs )
  cbx.var = tkinter.IntVar()
  cbx["variable"] = cbx.var
  tkinter.Checkbutton.checked = property( lambda x: x.var.get(), _setChecked )
  _x, _y = transformCoord(_x, _y)
  cbx.place(x = _x, y = _y)
  return cbx
#----------------------------------
def button(_text, _x, _y, **kwargs):
  btn = tkinter.Button(_win, text = _text, **kwargs)
  _x, _y = transformCoord(_x, _y)
  btn.place(x = _x, y = _y)
  return btn
#----------------------------------
def coords(obj):
  #return _C.coords(obj)
  return _C.bbox(obj)
#----------------------------------
def center(obj):
  x1, y1, x2, y2 = coords(obj)
  return (x1+x2)/2, (y1+y2)/2
#----------------------------------
def xCoord(obj):
  x1, y1, x2, y2 = coords(obj)
  return x1
#----------------------------------
def yCoord(obj):
  x1, y1, x2, y2 = coords(obj)
  return y1
#----------------------------------
def moveObjectTo(obj, x, y):
  x, y = transformCoord(x, y)
  coords = _C.coords(obj)
  _C.move(obj, x-coords[0], y-coords[1])
#----------------------------------
def moveObjectBy(obj, dx, dy):
  if _viewPort:
     x1, x2, y1, y2 = _viewPort
     w, h = windowSize()
     dx = dx*w/(x2 - x1)
     dy = - dy*h/(y2 - y1)
  _C.move(obj, dx, dy)
#----------------------------------
def deleteObject(obj):
  _C.delete(obj)
#----------------------------------
def changeCoords(obj, points):
  coord = unpackCoord(points)
  _C.coords(obj, *coord)
#----------------------------------
def changeProperty(obj, **kwargs):
  _C.itemconfigure(obj, **kwargs)
#----------------------------------
def changePenColor(obj, color):
  _C.itemconfigure(obj, outline=color)
#----------------------------------
def changeFillColor(obj, color):
  _C.itemconfigure(obj, fill=color)
#----------------------------------
def onMouseEvent(eventName, fn = None, btn = 0):
  eventStr = "<%s>" % eventName
  if btn == 0:
    if type(fn) == int:
      btn = fn
      fn = None
  if btn > 0:
    eventStr = "<%s-%d>" % (eventName, btn)
  _C.bind(eventStr, fn);
  listen()
#----------------------------------
def onMouseMove(fn = None):
  _C.bind("<Motion>", fn);
  listen()
def onMouseButtonMove(fn = None, btn = 0):
  _C.bind("<B1-Motion>", fn);
  listen()
def onMouseDown(fn = None, btn = 0):
  onMouseEvent("Button", fn, btn)
def onMouseUp(fn = None, btn = 0):
  onMouseEvent("ButtonRelease", fn, btn)
def onMouseClick(fn = None, btn = 0):
  onMouseUp(fn, btn)
def onMouseDblClick(fn = None, btn = 0):
  onMouseEvent("Double-Button", fn, btn)
#----------------------------------
def onMouseUp(fn = None, btn = 0):
  eventStr = "<ButtonRelease>"
  if btn == 0:
    if type(fn) == int:
      btn = fn
      fn = None
  if btn > 0:
    eventStr = "<ButtonRelease-%d>" % btn
  _C.bind(eventStr, fn);
  listen()
#----------------------------------
def onKey(keyStr, fn = None):
  if type(keyStr) == str:
    _C.bind("<KeyPress-%s>" % keyStr, fn);
  else:
    _C.bind("<KeyPress>", keyStr);
  listen()
#----------------------------------
def listen():
  _C.focus_force()
#----------------------------------
def onTimer(func, _time = -1):
  global _timerCalls
  if _time < 0: _time = 30
  timerId = onTimerCall(func, _time)
  _timerCalls.append( timerId )
  return timerId
#----------------------------------
def killTimer(timerId):
  global _timerCalls
  if timerId in _timerCalls:
    _timerCalls.remove( timerId )
    timerId.active = False
#----------------------------------
def runLoopFunc(timerCall):
  def timerFunc():
    if timerCall.active:
      timerCall.func()
      _win.after(timerCall.timeInterval, timerFunc)
  return timerFunc
#----------------------------------
def run():
  for timerCall in _timerCalls:
    runLoopFunc(timerCall)()
  _win.mainloop()
#----------------------------------
def close():
  _win.destroy()

###########################################
__initGraph__()
if __name__ == "__main__":
  windowSize ( 500, 250 )

  for i in range(0, 100, 10):
    line(0, 0, 100, i)

  penColor("red")
  for i in range(200, 100, -10):
    brushColor( randint(0,255),randint(0,255),randint(0,255))
    rectangle(100, 100, i, i)

  penColor("blue")
  for i in range(100, 0, -10):
    brushColor( randint(0,255),randint(0,255),randint(0,255))
    circle(300, 100, i)

  penColor("red")
  for i in range(10, 100, 10):
    brushColor( randint(0,255),randint(0,255),randint(0,255))
    polygon([(70,100), (150,i), (230,100), (70,100)])

  run()
