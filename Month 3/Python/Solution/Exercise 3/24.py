import datetime
today = datetime.datetime.now().date()
first_day_of_month = datetime.date(today.year, today.month, 1)
weekday_name = first_day_of_month.strftime("%A")
print(first_day_of_month,weekday_name)