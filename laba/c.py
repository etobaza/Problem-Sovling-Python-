n = int(input())
m = [0] * n 
for i in range(n): 
    m[i] = [0] * n

for j in range(n):
    m[0][j] = j 
    
for i in range(n):
    m[i][0] = i

for i in range(n):
    m[i][i] = i**2
    
for i in range(n):
    for j in range(n):
        print(m[i][j], end = ' ')
    print()
