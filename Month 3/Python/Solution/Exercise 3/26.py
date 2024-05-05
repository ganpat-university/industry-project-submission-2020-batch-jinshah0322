import datetime
today = datetime.datetime.now()
first_day_of_month = datetime.date(today.year, today.month, 1)
while first_day_of_month.weekday() != 0: 
    first_day_of_month += datetime.timedelta(days=1)
dates_of_week = []
for i in range(7):
    dates_of_week.append(first_day_of_month + datetime.timedelta(days=i))
print("Dates of the current week (Monday to Sunday):")
for date in dates_of_week:
    print(date)