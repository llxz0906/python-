import turtle as t
import random
import time
#设置背景
h=600
w=800
t.setup(width=w,height=h)
t.bgcolor("black")
t.ht()
#小鸟受重力影响向下掉落
g=-0.3#重力加速度
#小鸟类
class Bird:
    def initialize(self):
        #变成成员函数好重置
        self.y=h/3#小球y坐标
        self.x=-w/3#小球x坐标
        self.d=50#设置球的直径
        self.vy=0#球y方向的速度（掉落）
#想一想为什么这么设置？小鸟的起始位置有什么要求吗？
#如果一开始就在原点上会怎么样？
        self.score = 0  # 得分初始为0
        
    def draw(self):
        #绘制出小鸟
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.color("white")
        t.dot(self.d)#画一个直径为50的实心圆

         # 输出当前得分
        t.penup()  # 抬笔
        t.goto(-350, 220)  # 移到目标位置
        t.color('red')  # 红色
        t.write(str(self.score),align="center", font=("宋体", 28))
        #想一想为什么非得在小鸟类里写得分
        
    def update(self):
        #根据重力加速度更新小球速度
        self.vy=self.vy+g
        #根据速度更新小球y坐标（下落）
        self.y=self.y+self.vy
        #碰到下边界时，小鸟状态重置
        if self.y >= h/2-self.d/2 or self.y<=-h/2+self.d/2:
          #填什么?
            self.initialize()
    def flyup(self,x,y):
        self.vy=10#速度向上
        
# 水管类
class Pipe:  
    def initialize(self):  # 成员函数，对象初始化
        self.width = 40  # 初始化宽度
        self.gapHeight = h/2  # 中间空隙高度为画面高度一半
        self.xLeft = w/3  # 开始水管在画面右端
        self.xRight = w/3+self.width
        # 设定随机空隙上、下位置
        self.yGapTop = random.randint(20, h/2-20)
        self.yGapBottom = self.yGapTop - self.gapHeight
        self.vx = -2  # 向左运动的速度

    def draw(self):  # 成员函数，绘制水管
        t.color('yellow')  # 设为黄色
        # 绘制上部水管填充矩形
        t.penup()  # 抬笔
        t.goto(self.xLeft, h/2)  # 移动到坐标位置
        t.pendown()  # 落笔
        t.begin_fill()  # 开始填充
        t.goto(self.xRight, h/2)
        t.goto(self.xRight, self.yGapTop)
        t.goto(self.xLeft, self.yGapTop)
        t.end_fill()  # 结束填充
        # 绘制下部水管填充矩形
        t.penup()  # 抬笔
        t.goto(self.xLeft, self.yGapBottom)  # 移到坐标位置
        t.pendown()  # 落笔
        t.begin_fill()  # 开始填充
        t.goto(self.xRight, self.yGapBottom)
        t.goto(self.xRight, -h/2)
        t.goto(self.xLeft, -h/2)
        t.end_fill()  # 结束填充

    def update(self, b):  # 成员函数，水管更新
        if self.xRight < -w/2:  # 如果跑到最左边
            self.initialize()  # 初始化，在右边重新出现
            b.score = b.score + 1  # 得分增加
        self.xLeft = self.xLeft + self.vx  # 水管逐渐向左移动
        self.xRight = self.xLeft + self.width

        # 如果小鸟和水管碰撞
        if (b.x+b.d/2 > self.xLeft and
            b.x-b.d/2 < self.xRight and
            (b.y+b.d/2 > self.yGapTop or
             b.y-b.d/2 < self.yGapBottom)):
            b.score = 0  # 得分设为0

bird=Bird()#创建一个小鸟对象
bird.initialize()#小鸟对象初始化
pipe = Pipe()  # 创建水管对象
pipe.initialize()  # 水管对象初始化
#鼠标点击事件
t.onscreenclick(bird.flyup)#注意放置的位置
#让小鸟动起来
while True:
    t.tracer(False)
    t.clear()
    bird.draw()
    pipe.draw()  # 绘制水管
    t.tracer(True)
    pipe.update(bird)  # 更新水管
    bird.update()#更新小鸟
    time.sleep(0.01)


