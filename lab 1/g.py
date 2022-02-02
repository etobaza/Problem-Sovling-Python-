def toDecimal(n):
    sum = 0
    temp = 0
    for i in n:
        sum = sum + int(i)*(2**(len(n) - 1 - temp))
        temp += 1
    return sum
n = input()
print(toDecimal(n))