from turtle import *
import time

def drawBackground():
    #绘制中间的空心圆
    penup()
    goto(0,-50)
    setheading(0)
    pendown()
    color("red")
    circle(50)
    
class Needle:
    #针类
    angle=180#成员变量
    def draw(self):
        color("green")
        pensize(2)
        penup()
        goto(0,0)
        setheading(self.angle)#设定方向
        pendown()
        forward(150)
        
hideturtle()
setup(width=600,height=400)
needle=Needle()#针对象

while True:
    tracer(False)#隐藏绘图
    clear()
    needle.draw()
    drawBackground()
    tracer(True)
    time.sleep(0.01)
    
done()#结束
    
