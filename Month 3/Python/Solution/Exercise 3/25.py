import datetime
today = datetime.datetime.now().date()
first_day_of_first_month  = datetime.date(today.year, 1, 1)
weekday_name = first_day_of_first_month .strftime("%A")
print(first_day_of_first_month ,weekday_name)