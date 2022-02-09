import numpy as np 

n = int(input())
m = np.zeros((n, n), dtype = int)

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
