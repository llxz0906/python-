import datetime
brithday=input("出生日期(如2000-10-01):")
bday=datetime.datetime.strptime(brithday,'%Y-%m-%d')
today=datetime.datetime.now()
day=today-bday
print(day.days)
print(type(day.days))
print("你已经活了"+str(day.days)+"天")
