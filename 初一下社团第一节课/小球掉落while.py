from turtle import *
import time#导入时间处理模块
title("小球掉落")
speed(0)
ht()
y=200
while y>=-200:#小球y坐标递减
    tracer(False)#设置是否显示绘图中间过程
    clear()#清空屏幕
    penup()
    goto(0,y)
    pendown()
    dot(50,'red')#画直径为50的填充圆
    tracer(True)
    time.sleep(0.01)#暂停0.01毫秒
    y -=1
done()#绘制结束
