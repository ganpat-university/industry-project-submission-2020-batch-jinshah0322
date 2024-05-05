import datetime
today = datetime.datetime.now().date()
afterOneYear = today + datetime.timedelta(days=30)
print(afterOneYear)