import datetime
today = datetime.datetime.now()
bDay = datetime.datetime.strptime("2003-05-22","%Y-%m-%d")
differenceInDays = (today - bDay).days
print(differenceInDays)