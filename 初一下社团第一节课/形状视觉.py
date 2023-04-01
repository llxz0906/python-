from turtle import *
speed(10)
title("形状视觉")
i=0
for i in range(36):
    fd(500)#forward的缩写
    bk(500)#backward的缩写
    rt(10)
#射线
pu() # penup的缩写
bk(200)
pd() # pendown的缩写

lt(90)
fd(75)
rt(90)
#goto(x,y)
for i in range(4):
    fd(150)
    rt(90)
ht() # 隐藏乌龟

pu()
fd(320)
rt(90)
fd(150)
lt(90)
pd()
circle(75)
