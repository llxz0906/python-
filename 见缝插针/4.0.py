from turtle import *
import time

def drawBackground():
    penup()
    goto(0,-50)
    setheading(0)
    pendown()
    color("red")
    circle(50)
    
class Needle:
    angle=180
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

def addNeedle(x,y):
        newNeedle=Needle()
        needles.append(newNeedle)
        
hideturtle()
setup(width=600,height=400)
needles=[]
onscreenclick(addNeedle)

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
    
