from turtle import *
speed(0)
title("三色螺旋线")
angle=360/3+0.8
for i in range(225):
    if i%3 == 0:
        color("red")
    elif i%3 == 1:
        color("green")
    else:
        color("blue")
    forward(2*i)
    right(angle)
ht()
