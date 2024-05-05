import datetime
today = datetime.datetime.now().date()
one_week_from_today = today + datetime.timedelta(weeks=1)
print(one_week_from_today)