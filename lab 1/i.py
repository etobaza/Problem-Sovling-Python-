n = int(input())
i = 0
a = []
while i < n:
    string = str(input())
    a.append(string)
    i += 1
for i in range(n):
    strcur = a[i]
    if strcur[-10:] == "@gmail.com":
        print(strcur[0:len(strcur)-10])
        
