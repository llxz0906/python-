from turtle import *
import time

def drawBackground():
    #绘制实心圆
    penup()
    goto(0,-50)
    setheading(0)
    pendown()
    color("red")
    dot(50)
    
class Needle:
    #__init__(self,angle)
    angle=180#成员变量
    def draw(self):
        color("green")
        pensize(2)
        penup()
        goto(0,0)
        setheading(self.angle)
        pendown()
        forward(150)
    def update(self):
        self.angle=self.angle+1
        
hideturtle()
setup(width=600,height=400)
needle=Needle()#创建对象，对象名=类名（）

needles=[]
for a in range(0,360,10):
    newNeedle=Needle()
    newNeedle.angle=a
    needles.append(newNeedle)
while True:
    tracer(False)
    clear()
    for needle in needles:
        needle.update()
        needle.draw()
    drawBackground()
    tracer(True)
    time.sleep(0.01)
    
done()
    
