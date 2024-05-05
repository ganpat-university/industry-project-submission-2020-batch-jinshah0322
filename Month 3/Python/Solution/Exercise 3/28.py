import datetime
today = datetime.date.today()
first_day_of_month = today.replace(day=1)
if today.month == 12:  # If current month is December
    last_day_of_month = today.replace(year=today.year + 1, month=1, day=1) - datetime.timedelta(days=1)
else:
    last_day_of_month = today.replace(month=today.month + 1, day=1) - datetime.timedelta(days=1)
first_date_formatted = first_day_of_month.strftime("%dth %B %Y %A %I:%M:%S %p")
last_date_formatted = last_day_of_month.strftime("%dth %B %Y %A %I:%M:%S %p")

print("First date of the current month:", first_date_formatted)
print("Last date of the current month:", last_date_formatted)