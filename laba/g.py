from collections import defaultdict

n = int(input())
demon = defaultdict(int)
hunter = defaultdict(int)
temp = 0

for i in range(n):
    placeholder, penalty = input().split() #имя не требуется
    demon[penalty] += 1 #подсчет количества уязвимостей

m = int(input())
for i in range(m):
    placeholder, attack, gonna_kill = input().split() 
    hunter[attack] += int(gonna_kill)

for i in demon: #i в данном случае уязвимость
    if i in hunter:
        demon[i] = demon[i] - hunter[i]
    if demon[i]>0: 
        temp = temp + demon[i]

print("Demons left:", temp)