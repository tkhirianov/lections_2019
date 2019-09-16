import turtle
t = turtle.Turtle()
t.shape('turtle')
t.pensize(3)
t.color('green', 'yellow')

def polygone(length, edges_number):
    for i in range(edges_number):
        t.forward(length)
        t.left(360 / edges_number)

for length, x in [(10, 3), (50, 4), (100, 5), (70, 7)]:
    polygone(length, x)
    t.left(90)

t.hideturtle()
input()
