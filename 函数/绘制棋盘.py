from turtle import *
speed(0)
title("棋盘")
def line(x1,y1,x2,y2):
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)

step=15
for i in range(19):
    line(0,i*step,18*step,i*step)#水平
    line(i*step,0,i*step,18*step)#垂直
ht()
