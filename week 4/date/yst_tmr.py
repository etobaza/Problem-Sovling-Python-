import datetime

yes = datetime.datetime.now() - datetime.timedelta(1)
tdy = datetime.datetime.now()
tmr = datetime.datetime.now() + datetime.timedelta(1)
print("Yesterday:", yes.strftime("%d"))
print("Today:", tdy.strftime("%d"))
print("Tomorrow:", tmr.strftime("%d"))