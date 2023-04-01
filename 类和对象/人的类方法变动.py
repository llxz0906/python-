class person:
    def __init__(self,name,age,sex,song_name,dance_name):
        self.name=name
        self.age=age
        self.sex=sex
        self.song_name=song_name
        self.dance_name=dance_name
    def sing(self):
        print(self.name+"唱的是"+self.song_name)
    def dump(self):
        print(self.name+"跳的是"+self.dance_name)
    
zhangsan=person("张三","14","男","稻香","街舞1")
lisi=person("李四","12","女","我爱祖国","现代舞")
zhangsan.sing()
zhangsan.dump()
lisi.sing()
lisi.dump()

