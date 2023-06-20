from turtle import *
import time

def drawBackground():
    penup()
    goto(0,0)
    setheading(0)
    pendown()
    color("red")
    dot(100)
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
        self.angle=(self.angle+1)%360#注意要加1.不然会没办法动

def addNeedle(x,y):
    global gameover
    if gameover:
        return
    newNeedle=Needle()
    for needle in needles:#遍历原有列表，角度差
        if abs(needle.angle-newNeedle.angle)<4:#abs（）：绝对值
            gameover=True
            newNeedle.draw()#画新针，让效果展现出来
    needles.append(newNeedle)
        
hideturtle()
setup(width=600,height=400)
needles=[]
onscreenclick(addNeedle)
gameover=False
while not gameover:#gameover
    tracer(False)
    clear()
    for needle in needles:
        needle.update()
        needle.draw()
    drawBackground()
    tracer(True)
    time.sleep(0.01)
    
done()
    
