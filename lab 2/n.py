a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)

up = 0
down = len(a)-1
temp = []
for i in range(len(a)//2):
    sum = a[up]+a[down]
    up += 1
    down -= 1
    temp.append(sum)
middle = a[int(len(a)/2)]

if len(a)%2 == 0:
    print(*temp, " ")
else:
    print(*temp, middle, " ")