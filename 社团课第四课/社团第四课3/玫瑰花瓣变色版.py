from turtle import *
shape()
bgcolor("black")
number=int(numinput("圆的数量","玫瑰花瓣中圆的数量有多少？",6))
for x in range(number):
    pencolor("red")
    circle(100)
    left(360/number)
    pencolor("yellow")
    circle(50)
