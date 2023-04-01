import random
n=random.randint(0,100)
while True:
    a=int(input("输入猜的数字："))
    if a>n:
        print("大了")
    elif a<n:
        print("小了")
    else:
        print("猜对了")
        break
