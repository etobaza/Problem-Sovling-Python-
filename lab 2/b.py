n = int(input())
temp = input().split()
arr = []

for i in temp:
    arr.append(int(i))
arr.sort()
max1 = arr[n-1]
max2 = arr[n-2]
print(max1*max2)