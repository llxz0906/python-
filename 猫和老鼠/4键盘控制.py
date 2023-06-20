#游戏背景设置
import time
import turtle

global boxsize
boxsize=200#用于判断老鼠是否跑越界的一个值，最好是全局变量
mouse=turtle.Turtle()
cat=turtle.Turtle()
cat.shape("circle")#与老鼠区分
#老鼠先移动一段距离，避免一开始就被抓住
mouse.penup()
mouse.goto(100,100)

#老鼠移动同时也是响应按件事件的函数
#老鼠前进
def up():
    mouse.forward(10)
#老鼠后退
def back():
    mouse.backward(10)
#老鼠左转
def left():
    mouse.left(45)
#老鼠右转
def right():
    mouse.right(45)
#退出游戏
def quitTurtle():
    window.bye()
#判断老鼠是否越界
def checkbound():
    if mouse.xcor()>boxsize:
        mouse.goto(boxsize,mouse.ycor())  
    if mouse.xcor()<-boxsize:
        mouse.goto(-boxsize,mouse.ycor())
    if mouse.ycor()>boxsize:
        mouse.goto(mouse.xcor(),boxsize)
    if mouse.ycor()<-boxsize:
        mouse.goto(mouse.xcor(),-boxsize)
#键盘控制
window=turtle.Screen()#创建屏幕对象
#注册响应函数
window.onkeypress(up,"Up")      #按动方向键Up则执行函数up
window.onkeypress(left,"Left")
window.onkeypress(right,"Right")
window.onkeypress(back,"Down")
window.onkeypress(quitTurtle,"Escape")

# 让屏幕开始监听按键事件
window.listen()




