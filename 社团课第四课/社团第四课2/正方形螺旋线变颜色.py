import turtle
turtle.shape()
colors=["red","yellow","blue","green"]
for x in range(100):
    turtle.pencolor(colors[x%4])
    turtle.forward(x)
    turtle.left(91)
turtle.ht()
