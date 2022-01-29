def toLowercase(s):
    temp = ''
    for i in s:
        if(i >= 'A' and i <= 'Z'):
            temp = temp + chr((ord(i) + 32))
        else:
            temp = temp + i
    print(temp)

s = input()
toLowercase(s)