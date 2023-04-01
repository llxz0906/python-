#判断一个正整数是否是回文数
num=int(input("请输入一个正整数："))#input函数输入的内容的为字符串型，用int函数将其转换成整型
num1=str(num)[::-1]#切片操作指的是提取字符串的部分内容，要实现提取，就要先为字符串中的每个字符编号，在python中称为索引。
print(str(num),num1)
if str(num)==num1:
    print("是回文数")
if str(num)!=num1:
    print("不是回文数")
