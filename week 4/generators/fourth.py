def squares(len):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())
len = b - a 
len += 1
g = squares(len)

for i in range(len):
    print(next(g))
