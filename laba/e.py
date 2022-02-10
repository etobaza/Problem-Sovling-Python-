n = input().split()
if(len(n)<2): #когда инпут в две строки 
    x = int(input()) #икс в лист
    n.append(x) 

ntemp = int(n[0])
xtemp = int(n[1])
arr = []

for i in range(ntemp):
    arr.append(xtemp + 2*i)

res = arr[0]

for i in range(1, ntemp):
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



