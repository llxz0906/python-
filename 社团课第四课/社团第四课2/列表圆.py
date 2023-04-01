from turtle import *
shape()
bgcolor("black")
colors=["red","yellow","blue","green","orange","purple","white","gray"]
sides=int(numinput("数字大小","请输入数字（1-8）：",4,1,8))
for x in range(360):
    pencolor(colors[x%sides])
    forward(x*3/sides+x)
    left(360/sides+1)
    width(x*sides/200)
