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

    
zhangsan=person("张三","14","男")
print(zhangsan.name)
print(zhangsan.age)
print(zhangsan.sex)

zhangsan.sing()
zhangsan.dump()
zhangsan.rap()

print(zhangsan)
