# 导入所需的模块
import turtle
import time
import random

delay = 0.1#延时
score = 0#分数
high_score = 0#最高分


# 绘制窗口
wn = turtle.Screen()#创建turtle窗口
wn.title("贪吃蛇")
wn.bgcolor("blue")
# 用户可以自行调整窗口的长度与宽度
wn.setup(width=600, height=600)
wn.tracer(0)

# 蛇头
head = turtle.Turtle()#多支画笔——蛇
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"#蛇头移动方向的变量，stop表示不朝任何一个方向

# 游戏中的食物
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])#随机颜色
shapes = random.choice(['square', 'triangle', 'circle'])#随机形状的食物
food.speed(0)#食物不要动
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)#食物起始位置设置

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0, 250)
pen.write("得分 : 0， 最高得分 : 0", align="center",
          font=("candara", 24, "bold"))


# 设定按键方向

def group():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(group, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

segments = []#在游戏开始时， segment 列表是一个空列表。当蛇头吃到食物时，会在游戏画布上增加一个分段。


# 游戏主程序
while True:
    wn.update()#更新画布
    #判断是否与边界相撞。如果蛇头超出了屏幕边界（即超过了 290 或小于 -290），则游戏结束。
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)#将蛇头移动到屏幕中央 (0, 0) 处，让它暂停一秒钟。
        head.goto(0, 0)
        #产生一个新的随机颜色和形状，让食物生成在屏幕中央位置。
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        #将已经存在的蛇身分段都移到屏幕外，清空 segments 列表，将得分归零，将延时设为 0.1。
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {}， High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    #蛇吃到食物的判断
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # 蛇添加分段
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # 尾巴颜色
        new_segment.penup()
        #将新的分段对象 new_segment 添加到 segment 列表中，用于在下一轮循环中更新分段的位置。
        segments.append(new_segment)
        delay -= 0.001#减少延时
        score += 10#分数+10
        #记录最高分
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("得分 : {}， 最高得分 : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
  
    #从后往前遍历列表，取出前一个分段的位置，并将当前分段移动到前一个分段的位置上。
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #判断蛇是否有分段，如果有则将 segments[0] 的位置更新为蛇头的位置
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    #蛇运动
    move()




    
    #循环用于判断蛇头是否与蛇身相撞，遍历 segment 列表中的所有分段.
    #判断它们与蛇头的距离是否小于 20，如果小于 20，则表示蛇头与蛇身相撞。
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("得分 : {}, 最高得分 : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)#设置循环后的时间休息，用于控制蛇的移动速度。

wn.mainloop()
