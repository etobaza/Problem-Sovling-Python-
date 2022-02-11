n = int(input())
shelf = []
picked = []

for i in range(n):
    s = input()
    if int(s[0]) == 1:
        razdel = s.split()
        shelf.append(razdel[1])
    if int(s[0]) == 2:
        picked.append(shelf[0])
        del shelf[0]
  
for i in range(len(picked)):
    print(picked[i], end = " ")