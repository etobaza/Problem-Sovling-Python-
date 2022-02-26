def isEven(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())
gen = isEven(n)
n=n//2+1

for i in range(n-1):
    print(next(gen), end=', ')
print(next(gen))
