import turtle
t = turtle.Turtle()
screen = turtle.Screen()

t.fillcolor("red")
t.begin_fill()
for _ in range(3):
    t.forward(150)
    t.left(120)
t.end_fill()

turtle.done()