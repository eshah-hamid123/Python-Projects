import datetime as dt

now = dt.datetime.now()
print(now)
year = now.year
print(year)
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2002, month=3, day=6, hour=9)
print(date_of_birth)


