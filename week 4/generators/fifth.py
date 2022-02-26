def generator(n):
    for i in range(0, n+1):
        yield i


n = int(input())
g = generator(n)
temp = []
for i in range(n):
    temp.append(next(g))
temp.reverse()
for i in range(n):
    print(temp[i])
