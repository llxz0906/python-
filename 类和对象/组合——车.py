class Car:
    def __init__(self,name,power = None):
        self.__name = name
        self.__power = power

    def set_power(self,power):
        self.__power = power

    def zhuang_tread(self):
        print(self.__name+"装好了"+self.__power.get_name()+"的轮胎")

    def zhuang_engine(self):
        print(self.__name+"装好了"+self.__power.get_name()+"的发动机")

class Tread:
    def __init__(self,name):
        self.__name = name

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

class Engine:
    def __init__(self,name):
        self.__name = name

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name


tread = Tread("厉害牌")
engine = Engine("赛车")
car = Car("奔驰",tread)
car.zhuang_tread()
car.set_power(engine)
car.zhuang_engine()

