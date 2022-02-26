import datetime

date = datetime.datetime.now() - datetime.timedelta(5)

print(date.strftime("%d"))