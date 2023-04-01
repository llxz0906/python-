
from turtle import *
shape()
penup()
bgcolor("black")
sides=int(numinput("边的数量","你想螺旋线有几条边？（2-6）",4,2,6))
colors=["red","yellow","blue","green","purple","orange"]
for m in range(100):
    forward(m*4)
    p=position()
    h=heading()
    print(position,heading)
    for n in range(int(m/2)):
        pendown()
        pencolor(colors[n%sides])
        forward(2*n)
        right(360/sides-2)
        penup()
    setx(p[0])
    sety(p[1])
    setheading(h)
    left(360/sides+2)
