import turtle as t
import random
import time
#设置背景
h=600
w=800
t.setup(width=w,height=h)
t.bgcolor("black")
t.ht()
#小鸟受重力影响向下掉落
g=-0.3#重力加速度，设置变量时，在用它之前一定要定义好
#小鸟类
class Bird:
    def initialize(self):
        #变成成员函数好重置
        self.y=h/3#小球y坐标
        self.x=-w/3#小球x坐标
        self.d=50#设置球的直径
        self.vy=0#球y方向的速度（掉落）
#想一想为什么这么设置？小鸟的起始位置有什么要求吗？
#如果一开始就在原点上会怎么样？
    def draw(self):
        #绘制出小鸟
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.color("white")
        t.dot(self.d)#画一个直径为50的实心圆
    def update(self):
        #根据重力加速度更新小球速度
        self.vy=self.vy+g
        #根据速度更新小球y坐标（下落）
        self.y=self.y+self.vy
        #碰到下边界时，小鸟状态重置
        if self.y >= h/2-self.d/2 or self.y<=-h/2+self.d/2:
          #填什么?
            self.initialize()
#因为你要重复用它，所以把初始化函数变成成员函数，这样可以方便调用
            
bird=Bird()#创建一个小鸟对象
bird.initialize()#小鸟对象初始化

#让小鸟动起来
while True:
    t.tracer(False)
    t.clear()
    bird.draw()
    t.tracer(True)
    bird.update()#更新小鸟
    time.sleep(0.01)


