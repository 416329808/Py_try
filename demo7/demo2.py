import datetime
now = datetime.datetime.now()
print(now.date())
deita = now .date() - datetime.date(now.year-1, 12, 31)
week = (deita.days // 7) + 1
week_days = deita.days % 7 + 1
print(week, week_days)