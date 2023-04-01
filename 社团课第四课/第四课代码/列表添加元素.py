
name=[]#创建一个空列表，并把它赋值给变量name
name.append("小张")#在列表中陆续添加学生姓名“小张”和“小李”
name.append("小李")
print(name)
name.extend(["小黄","小曹","小孟"])#在列表的末尾依次添加学生姓名“小黄”“小曹”“小孟”
print(name)
name.insert(2,"小冯")#在列表的第二个索引位置（即第三个元素）之前插入学生姓名“小冯”
print(name)
name[0]="小何"#将列表中第0个索引位置（即第一个元素）的学生姓名更改为“小何”
print(name)

