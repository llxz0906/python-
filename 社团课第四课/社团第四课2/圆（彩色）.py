from turtle import *
shape()
speed(10)
bgcolor("black")
colors=["red","yellow","blue","green"]
for x in range(100):
    pencolor(colors[x%4])
    circle(x)
    left(91)
