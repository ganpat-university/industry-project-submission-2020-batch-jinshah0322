import datetime
today = datetime.datetime.now().date()
afterOneYear = today + datetime.timedelta(days=365)
print(afterOneYear)