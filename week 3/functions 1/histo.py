def histogram(l):
    for i in l:
       stars = i*"*"
       print(stars)

list = input().split()
for i in range(0, len(list)):
    list[i] = int(list[i])
    
histogram(list)
