class person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def __str__(self):
        info="姓名："+self.name+"年龄："+self.age+"性别："+self.sex
        return info
    def sing(self,seq,music):
        print(self.name+"第"+seq+"个唱"+music)
    def sing(self,music):
        print(self.name+"唱"+music)
    def dump(self):
        print("跳得真好听")
    def rap(self):
        print("rap不错")
lili=person("丽丽","13","女")
lili.sing("海阔天空")
