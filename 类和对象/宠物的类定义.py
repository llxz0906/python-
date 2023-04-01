class pet:
    def __init__(self,name,age,sex,color):
        self.name=name
        self.age=age
        self.sex=sex
        self.color=color
    def eat(self):
        print("吃的方法")
    def say(self):
        print("叫的方法")

cat=pet("大胖橘","2","公","橘色")
print(cat.name)
print(cat.age)
print(cat.sex)
print(cat.color)
