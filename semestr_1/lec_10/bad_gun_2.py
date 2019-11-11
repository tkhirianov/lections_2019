from random import randrange as rnd, choice
import tkinter as tk
from tkinter import *
import math
from math import *
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


def SHAR(n):
    global shar_x, shar_y, shar_r, shar_vx, shar_vx0, shar_vy, shar_vy0, shar_ris, shar_cvet, shar_t, shar_kol
    shar_vx[n] = shar_vx[n] // 1
    shar_vx0[n] = shar_vx[n]
    shar_vy0[n] = shar_vy[n]
    shar_vy[n] = (shar_vy[n] // 1) - 1
    if shar_x[n] >= 790 - shar_r[n]:
        shar_vx[n] = -abs(shar_vx[n])
    if shar_x[n] <= shar_r[n] + 10:
        shar_vx[n] = abs(shar_vx[n])
    if shar_y[n] >= 590 - shar_r[n]:
        shar_vy[n] = (abs(shar_vy[n]))
    if shar_y[n] <= shar_r[n] + 10:
        shar_vy[n] = -abs(shar_vy[n])
    shar_x[n] += (shar_vx[n] + shar_vx0[n]) // 2
    shar_y[n] -= (shar_vy[n] + shar_vy0[n]) // 2
    canv.delete(shar_ris[n])
    shar_ris[n] = canv.create_oval(shar_x[n] - shar_r[n], shar_y[n] - shar_r[n], shar_x[n] + shar_r[n],
                                   shar_y[n] + shar_r[n], fill=shar_cvet[n])


def PUSHKA_PRICEL(event):
    global ugol, q, sila, pushka
    if event:
        if (event.x - 20 > 0):
            ugol = math.atan((450 - event.y) / (event.x - 20))
        elif (event.x - 20 < 0):
            ugol = pi + math.atan((450 - event.y) / (event.x - 20))
        else:
            ugol = pi
    if (q == 1):
        c = 'orange'
    else:
        c = 'black'
    canv.delete(pushka)
    pushka = canv.create_line(20, 450, 20 + (sila + 2) * cos(ugol) * 20, 450 - (sila + 2) * sin(ugol) * 20, width=7,
                              fill=c)


def ZAPUSK1(event):
    global q
    q = 1


def SILA():
    global sila, q
    if (q == 1 and sila < 3):
        sila = sila + 0.1
    print(sila)


def ZAPUSK2(event):
    global sila, q, ugol, shar_x, shar_y, shar_r, shar_vx, shar_vx0, shar_vy, shar_vy0, shar_ris, shar_cvet, shar_t, shar_kol
    q = 0
    i = 0
    z = 0
    print(sila)
    while z != 1:
        if (shar_ris[i] == 0):
            shar_x[i] = 20 + (sila + 2) * cos(ugol) * 20
            shar_y[i] = 450 - (sila + 2) * sin(ugol) * 20
            shar_r[i] = 20
            shar_vx[i] = (sila + 0.2) * cos(ugol) * 20
            shar_vx0[i] = shar_vx[i]
            shar_vy[i] = (sila + 0.2) * sin(ugol) * 20
            shar_vy0[i] = shar_vy[i]
            shar_cvet[i] = "blue"
            shar_t[i] = 100
            z = 1
            shar_kol = shar_kol + 1
            sila = 0
            PUSHKA_PRICEL('')
        elif (i >= len(shar_r) - 1):
            shar_ris.append(0)
            shar_x.append(0)
            shar_y.append(0)
            shar_vx.append(0)
            shar_vx0.append(0)
            shar_vy.append(0)
            shar_vy0.append(0)
            shar_r.append(0)
            shar_cvet.append(0)
            shar_t.append(0)
        i = i + 1


def CEL(n):
    global cel_x, cel_y, cel_vx, cel_vy, cel_r, cel_ris
    cel_x[n] = cel_x[n] + cel_vx[n]
    cel_y[n] = cel_y[n] + cel_vy[n]
    canv.delete(cel_ris[n])
    cel_ris[n] = canv.create_oval(cel_x[n] - cel_r[n], cel_y[n] - cel_r[n], cel_x[n] + cel_r[n], cel_y[n] + cel_r[n],
                                  fill="red")


screen1 = canv.create_text(400, 300, text='', font='28')


def new_game(event=''):
    global screen1, shar_x, shar_y, shar_vx, shar_vx0, shar_vy, shar_vy0, shar_cvet, shar_t, shar_r, shar_ris, shar_kol, q, cel_x, cel_y, cel_vx, cel_vy, cel_r, cel_ris, pushka, sila, ugol
    canv.update()
    canv.itemconfig(screen1, text='')
    q = 0
    sila = 0
    pushka = 0
    ugol = 0
    shar_x = [0]
    shar_y = [0]
    shar_r = [-1]
    shar_vx = [0]
    shar_vx0 = [0]
    shar_vy = [0]
    shar_vy0 = [0]
    shar_t = [0]
    shar_cvet = [0]
    shar_ris = [0]
    shar_kol = 0
    m = 3
    cel_x = [0] * m
    cel_y = [0] * m
    cel_r = [0] * m
    cel_ris = [0] * m
    cel_vx = [0] * m
    cel_vy = [10] * m
    PUSHKA_PRICEL('')
    canv.bind('<Button-1>', ZAPUSK1)
    canv.bind('<ButtonRelease-1>', ZAPUSK2)
    canv.bind('<Motion>', PUSHKA_PRICEL)
    z = 3
    for p in range(0, 3):
        cel_x[p] = rnd(600, 780)
        cel_y[p] = rnd(50, 550)
        cel_r[p] = rnd(20, 50)
        cel_vx[p] == 0
    while z != 0:
        for p in range(0, 3):
            if (cel_y[p] >= 550):
                cel_vy[p] = -10
            elif (cel_y[p] <= 50):
                cel_vy[p] = 10
            CEL(p)
        b = 0
        SILA()
        while (b < len(shar_r)):
            if (shar_t[b] < 0 and shar_r[b] != -1 and len(shar_r) >= 2):
                canv.delete(shar_ris[b])
                del shar_ris[b]
                del shar_x[b]
                del shar_y[b]
                del shar_vx[b]
                del shar_vx0[b]
                del shar_vy[b]
                del shar_vy0[b]
                del shar_r[b]
                del shar_cvet[b]
                del shar_t[b]
                b = b - 1
            elif (len(shar_r) == 1 and shar_t[b] < 0 and shar_r[b] != -1):
                canv.delete(shar_ris[b])
                shar_ris[b] = 0
                shar_x[b] = 0
                shar_y[b] = 0
                shar_vx[b] = 0
                shar_vx0[b] = 0
                shar_vy[b] = 0
                shar_vy0[b] = 0
                shar_r[b] = -1
                shar_cvet[b] = 0
                shar_t[b] = 0
            elif (shar_r[b] != -1):
                SHAR(b)
                shar_t[b] = shar_t[b] - 1
                for p in range(0, 3):
                    if ((shar_x[b] - cel_x[p]) ** 2 + (shar_y[b] - cel_y[p]) ** 2 <= (shar_r[b] + cel_r[p]) ** 2):
                        cel_x[p] = 2000
                        cel_y[p] = 300
                        cel_vx[p] = 0
                        cel_vy[p] = 0
                        z = z - 1
            b = b + 1
        time.sleep(0.03)
        canv.update()

    canv.bind('<Motion>', '')
    canv.bind('<Button-1>', '')
    canv.bind('<ButtonRelease-1>', '')
    canv.delete(ALL)
    screen1 = canv.create_text(400, 300, text='', font='28')
    canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(shar_kol) + ' выстрелов')
    root.after(1800, new_game)


new_game()

mainloop()
