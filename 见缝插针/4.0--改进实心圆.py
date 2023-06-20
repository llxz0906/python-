from turtle import *
import time

def drawBackground():
    #实心圆
    penup()
    goto(0,0)
    setheading(0)
    pendown()
    color("red")
    dot(100)
    #起点的针
    penup()
    goto(-300,0)
    color("green")
    pensize(2)
    pendown()
    goto(-180,0)
    
class Needle:
    angle=180
    def draw(self):
        color("green")
        pensize(2)
        penup()
        goto(0,0)
        setheading(self.angle)
        pendown()
        forward(50)
        pendown()
        forward(100)
    def update(self):
        self.angle=self.angle+1
#添加针的函数
def addNeedle(x,y):
        newNeedle=Needle()
        needles.append(newNeedle)
        
hideturtle()
setup(width=600,height=400)
needles=[]
onscreenclick(addNeedle)#addNeedle函数注册到鼠标单击屏幕的事件中

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
    
