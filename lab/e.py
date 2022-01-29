n = input().split()
dist = int(n[0])
ammo = int(n[1])

notprime = False
prime = 1
if dist > 1:
    for i in range(2, dist):
        if (dist % i) == 0:
            notprime = True
            break

if notprime:
    prime = 0

if dist <= 500 and prime == 1 and ammo % 2 == 0:
    print("Good job!")
else:
    print("Try next time!")