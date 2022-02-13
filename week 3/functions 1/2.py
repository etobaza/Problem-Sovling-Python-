def toCentigrade(Fahrenheit):
    temp = (5/9)*(Fahrenheit - 32)
    return round(temp, 2)

f = int(input())
print(toCentigrade(f))