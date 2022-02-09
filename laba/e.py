n, x = map(int, input().split())
arr = []

for i in range(n):
    arr.append(x + 2*i)

res = arr[0]

for i in range(1, n):
    res = res^arr[i]

print(res)

"""
5(10) = 101(2)

011
101
110

110
111
001

0001
0101
0100


a b  a^b
1 1  0
1 0  1
0 1  1
0 0  0
"""



