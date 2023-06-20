from turtle import *
import time
def drawBackground():
    #绘制中间的空心圆
    penup()
    goto(0,0)
    setheading(0)
    pendown()
    color("red")
    dot(50)
    
class Needle:
    #针类
    angle=180#成员变量
    #def __init__(self,angle):
        #self.angle=angle
    def draw(self):
        color("green")
        pensize(2)
        penup()
        goto(0,0)
        setheading(self.angle)#设定方向
        pendown()
        forward(150)
    def update(self):
        #self.angle=self.angle+1
        #self.angle++
        self.angle+=1
        
needle=Needle()
hideturtle()
setup(width=600,height=400)
while True:#知道次数的用for，不知道次数的用while
    tracer(False)#隐藏
    clear()#清屏
    needle.update()
    needle.draw()#针类的绘制方法调用
    drawBackground()
    tracer(True)
    time.sleep(0.01)#暂停0.01毫秒
done()#绘制结束
















