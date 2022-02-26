import datetime

date1 = datetime.datetime(1914, 7, 28, 12, 50, 2)
date2 = datetime.datetime(1914, 7, 28, 7, 40, 4)
print((date1 - date2).total_seconds())