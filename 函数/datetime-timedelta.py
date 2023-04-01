import datetime
today=datetime.datetime.today()
print(today)
print(type(today))
one=datetime.timedelta(days=1)
yesterday=today-one
print(yesterday)
tomorrow=today+one
print(tomorrow)
#时间推后一个月
month=one*31
nextmonth=today+month
print(nextmonth)
