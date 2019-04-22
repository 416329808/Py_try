import datetime
[year, month, day] = map(int, input("请输入年月日:").split())
targetDay = datetime.date(year, month, day)#输入的日期作为一个datatime
deita = targetDay - datetime.date(targetDay.year-1, 12, 31)#上一年最后一天的日期
print('%d年%d月%d日是%d的第%d天' %(year, month, day, year, deita.days))#输出deita的天数
