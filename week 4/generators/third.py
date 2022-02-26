def mamba(n):
    for i in range(0, n+1, 12):
        yield i

n = int(input())
g = mamba(n)

for i in range(0, n//12+1):
    print(next(g))
