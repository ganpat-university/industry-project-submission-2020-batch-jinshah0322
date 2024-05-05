import datetime
today = datetime.date.today()
first_day_of_month = datetime.date(today.year,today.month,1)
if today.month == 12: 
    last_day_of_month = today.replace(year=today.year + 1, month=1, day=1) - datetime.timedelta(days=1)
else:
    last_day_of_month = today.replace(month=today.month + 1, day=1) - datetime.timedelta(days=1)

print("First date of the current month:", first_day_of_month)
print("Last date of the current month:", last_day_of_month)