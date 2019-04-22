import datetime
now = datetime.datetime.now()
print('当前的日期为:', now.date(), end='')
deita = now .date() - datetime.date(now.year-1, 12, 31)
week = (deita.days // 7) + 1
week_days = deita.days % 7 + 1
print('是%d的第%d个周的第%d天' %(now.year, week, week_days))
