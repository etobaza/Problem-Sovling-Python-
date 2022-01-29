a = []
n = int(input())
i=0

while i < n:
    temp = int(input())
    a.append(temp)
    i += 1
for i in range(n):
    if a[i] <= 10:
        print("Go to work!")
    elif a[i] > 10 and a[i] <= 25:
        print("You are weak")
    elif a[i] > 25 and a[i] <= 45:
        print("Okay, fine")
    else:
        print("Burn! Burn! Burn Young!")