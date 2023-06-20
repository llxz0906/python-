import turtle  as t# 导入turtle绘图库
h = 600  # 窗口高度
w = 800  # 窗口宽度
t.setup(width=w, height=h)  # 设置绘图窗口大小
t.bgpic("background.gif")  # 显示背景图片
birdImage = "bird.gif"  # 小鸟图片
t.addshape(birdImage)  # 把小鸟图片添加到画笔候选显示图形
t.shape(birdImage)  # 画笔显示为小鸟图片
t.showturtle()  # 显示画笔图形
t.done()  # 绘制结束
