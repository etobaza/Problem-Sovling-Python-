s = input().split()
arr = []
for i in range(len(s)):
    arr.append(''.join(temp for temp in s[i] if temp.isalnum())) #исключить лишнее

arr = list(dict.fromkeys(arr)) #удаление копий
arr = sorted(arr) #сортировка

print(len(arr))
for i in range(len(arr)):
    print(arr[i])
