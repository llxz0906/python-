class person:
    def __init__(self,name,sex):
        self.name=name
        self.__age=None
        self.sex=sex
    def __str__(self):
        info="姓名："+self.name+"性别："+self.sex
        return info
    def sing(self):
        print("唱得真好听")
    def dump(self):
        print("跳得真好听")
    def rap(self):
        print("rap不错")
    def set(self,age):
        self.__age=age
    def get(self):
        return self.__age
libai=person("李白","男")
libai.set(32)
print(libai.get())
