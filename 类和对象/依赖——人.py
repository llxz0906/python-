#依赖
class Person:
    def run(self):
        print("我没事干")

class Computer:
    def play(self,tool):
        tool.run()#调用了Person类中的方法
        print("我是电脑，玩我")


class Phone:
    def play(self,tool):
        tool.run()#调用了Person类中的方法
        print("我有王者荣耀，来玩啊")

zhangsan = Person()
dnf = Computer()
dnf.play(zhangsan)   #依赖是给一个类的对象的方法给另一个对象

wangzhe = Phone()
wangzhe.play(zhangsan)
