import tkinter as tk
from random import randint

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self):
        self.R = randint(20, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (+2, +3)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                     self.y - self.R,
                                     self.x + self.R,
                                     self.y + self.R, fill="green")

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def canvas_click_handler(event):
    print('Hello World! x=', event.x, 'y=', event.y)


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


def main():
    global root, canvas, balls
    
    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw", fill=tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)
    balls = [Ball() for i in range(5)]
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
