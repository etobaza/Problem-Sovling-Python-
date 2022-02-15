import math

def filter_prime(checklist):
    prime = []
    for i in checklist:
        Flag = True
        for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    Flag = False
                    break
        if Flag == True and i>1:
                prime.append(i)
    return prime


list = input().split()
for i in range(0, len(list)):
    list[i] = int(list[i])
print(*filter_prime(list))

