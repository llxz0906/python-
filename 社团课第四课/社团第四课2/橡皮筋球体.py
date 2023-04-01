from turtle import *
shape()
bgcolor("black")
speed(10)
sides=6
colors=["red","yellow","blue","orange","green","purple"]
for x in range(360):
    pencolor(colors[x%sides])
    forward(x*3/sides+x)
    left(360/sides+1)
    pensize(x*sides/200)
    left(90)
ht()
