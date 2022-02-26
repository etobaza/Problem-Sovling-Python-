import datetime

date = datetime.datetime.now()
date = date.replace(microsecond=0)

print(date)