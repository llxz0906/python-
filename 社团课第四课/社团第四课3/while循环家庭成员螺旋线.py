
from turtle import *
shape()
bgcolor("black")
colors=["red","yellow","blue","green",
        "orange","purple","white","brown","gray","pink"]
family=[]
name=textinput("我的家人","输入一个名字否则按回车键结束：")
while name!="":
    family.append(name)
    name=textinput("我的家人","输入一个名字否则按回车键结束:")
for x in range(100):
    pencolor(colors[x%len(family)])
    penup()
    forward(x*4)
    pendown()
    write(family[x%len(family)],font=("YouYuan",int((x+4)/4),"bold"))
    left(360/len(family)+2)
    
