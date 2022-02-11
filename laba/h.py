from math import sqrt

def howfar(arr): 
    return arr[1] 

temp = []
x1, y1 = map(int, input().split())
n = int(input())

for i in range(n):
    x2, y2 = map(int, input().split())
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    temp.append(((x2, y2), distance))

temp.sort(key=howfar) #сортируем по дистанции от начала координат

for i in temp:
    coordinates = i[0]
    print(*coordinates)