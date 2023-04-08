class person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def __str__(self):
        info="姓名："+self.name+"年龄："+self.age+"性别："+self.sex
        return info
    def sing(self):
        print("唱得真好听")
    def dump(self):
        print("跳得真好听")
    def rap(self):
        print("rap不错")

class girl(person):
    def run(self):
        print("跑得真快")
    def sing(self):
        print("唱青藏高原")

lili=girl("丽丽","13","女")
lili.sing()
