from turtle import *
shape()
bgcolor("black")
colors=["red","yellow","blue","green"]
name=textinput("输入你的名字","你的名字是什么？")
for x in range(100):
    pencolor(colors[x%4])
    penup()
    forward(x*4)
    pendown()
    write(name,font=("YouYuan",int((x+4)/4),"bold"))
    left(92)
