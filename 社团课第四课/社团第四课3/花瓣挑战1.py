from turtle import *
shape()
penup()
bgcolor("black")
speed(10)
sides=int(numinput("边的数量","你想螺旋线有几条边？（2-6）",4,2,6))
colors=["red","yellow","blue","green","purple","orange"]
for m in range(100):
    forward(m*4)
    p=position()
    h=heading()
    print(position,heading)
    for n in range(sides):
        pendown()
        pencolor(colors[n%sides])
        circle(m/5)
        right(360/sides-2)
        pensize(m/20)
        penup()
    setx(p[0])
    sety(p[1])
    setheading(h)
    left(360/sides+2)
