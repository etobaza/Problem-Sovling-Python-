s = input().split()
arr = []
for i in range(len(s)):
    arr.append(''.join(temp for temp in s[i] if temp.isalnum()))

arr = list(dict.fromkeys(arr))
arr = sorted(arr)

print(len(arr))
for i in range(len(arr)):
    print(arr[i])
