import turtle as t
import random
import time
#设置背景
h=600
w=800
t.setup(width=w,height=h)
t.bgcolor("black")
t.ht()
#小鸟类
class Bird:
    def __init__(self,x,y,d):
        self.x=-x#小球x坐标
        self.y=y#小球y坐标
        self.d=d#设置球的直径
#想一想为什么这么设置？小鸟的起始位置有什么要求吗？
#如果一开始就在原点上会怎么样？
    def draw(self):
        #绘制出小鸟
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.color("white")
        t.dot(self.d)#画一个直径为50的实心圆
bird=Bird(-266,200,50)#创建一个小鸟对象
