from turtle import *
import time#导入时间处理模块
title("小球掉落")
speed(0)
ht()
for y in range(200,-201,-1):#小球y坐标递减
    penup()
    goto(0,y)
    pendown()
    dot(50,'red')#画直径为50的填充圆
done()#绘制结束
