from tkinter import *


def handler1(event):
    print('Hello World! x=', event.x, 'y=', event.y)


def handler2(event):
    exit()


# инициализация
root = Tk()
hello_label = Label(root, text="Hello, world!", font="Times 40")  
hello_label.pack()

# Привязка обработчиков - к событию и виджету:
#виджет.bind(событие, обработчик)
hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-3>', handler2)


# главный цикл (проект)
root.mainloop()

print('Программа заканчивается. Вышли из главного цикла.')
