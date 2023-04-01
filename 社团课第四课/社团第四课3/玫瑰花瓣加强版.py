from turtle import *
shape()
number=int(numinput("圆的数量","玫瑰花瓣中圆的数量有多少？",6))
for x in range(number):
    circle(100)
    left(360/number)
