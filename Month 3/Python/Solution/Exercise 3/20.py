import datetime
today = datetime.datetime.now()
bDay = datetime.datetime.strptime("2003-05-22","%Y-%m-%d")
differenceInDays = (today - bDay).days
years = differenceInDays//365
daysLeftFromYears = differenceInDays % 365
months = daysLeftFromYears//30
daysLeftFromMonths = months % 30
print(f"Years={int(years)},Months={int(months)},Days={daysLeftFromMonths}")