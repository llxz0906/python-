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
