import tkinter as tk
from random import randint

WIDTH = 300
HEIGHT = 200

def canvas_click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)

def tick():
    global x, y, dx, dy
    x += dx
    y += dy
    if x + R > WIDTH or x - R <= 0:
        dx = -dx
    if y + R > HEIGHT or y - R <= 0:
        dy = -dy

    canvas.move(ball_id, dx, dy)
    root.after(50, tick)


def main():
    global root, canvas
    global ball_id, x, y, dx, dy, R  # TODO: сделать объекно-ориентированный рефакторинг
    
    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw", fill=tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)

    R = randint(20, 50)
    x = randint(R, WIDTH - R)
    y = randint(R, HEIGHT - R)
    dx, dy = (+2, +3)
    ball_id = canvas.create_oval(x - R, y - R, x + R, y + R, fill="green")

    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
