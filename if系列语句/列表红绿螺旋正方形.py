from turtle import *
colors=["red","green"]
for i in range(100):
    pencolor(colors[i%2])
    forward(i)
    right(91)
ht()

