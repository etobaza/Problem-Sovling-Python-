info = int(input())
type = str(input())

if type == "k":
    precision = int(input())
    info = info / 1024
    round(info, precision)
    print(info)
else:
    info = info*1024
    print(info)