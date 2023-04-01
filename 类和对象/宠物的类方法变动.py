class pet:
    def __init__(self,name,age,sex,color,food,sound):
        self.name=name
        self.age=age
        self.sex=sex
        self.color=color
        self.food=food
        self.sound=sound
    def eat(self):
        print(self.name+"吃"+self.food)
    def say(self):
        print(self.name+self.sound+"叫")

cat=pet("大胖橘","2","公","橘色","猫粮","喵喵")
dog=pet("旺财","3","公","黑色","狗粮","汪汪")
cat.eat()
cat.say()
dog.eat()
dog.say()
