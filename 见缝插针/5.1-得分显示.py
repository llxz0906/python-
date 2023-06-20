from turtle import *
import time
color('blue')
write("这是一个见缝插针的游戏",align="center",font=("宋体",40))
time.sleep(5)
ht()
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
    #得分文字部分
    color("black")
    n=str(len(needles))#针的个数
    penup()
    goto(-240,10)
    write(n,align="center",font=("宋体",18))
    if gameover:
        penup()
        goto(-240,-40)
        color("black")
        write("游戏结束",align="center",font=("宋体",18))
    
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
        self.angle=(self.angle+1)%360

def addNeedle(x,y):
    global gameover
    if gameover:
        return
    newNeedle=Needle()
    for needle in needles:
        if abs(needle.angle-newNeedle.angle)<4:
            gameover=True
            newNeedle.draw()
    needles.append(newNeedle)
        
hideturtle()
setup(width=600,height=400)
needles=[]
onscreenclick(addNeedle)
gameover=False
while not gameover:
    tracer(False)
    clear()
    for needle in needles:
        needle.update()
        needle.draw()
    drawBackground()
    tracer(True)
    time.sleep(0.01)
    
done()
    
