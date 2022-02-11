n = int(input())
arr = []
a = ""
for i in range(n):
    a = input()
    arr.append(a)

def upCheck(s):
    for i in s:
        if i >= 'A' and i <= 'Z':
            return True
            break

def lowCheck(s):
    for i in s:
        if i >= 'a' and i <= 'z':
            return True
            break

def digit(s):
    for i in s:
        if i >= '0' and i <= '9':
            return True
            break

def strong(s):
    if upCheck(s) == True and lowCheck(s) == True and digit(s) == True:
        return True

fake_set = set(arr) #избавляюсь от повторений с списке имен
bkar = list(fake_set) #back_to_array, возвращаю set обратно в список
bkar.sort() #сортировка порядка имен в списке

arr2 = []
cnt = 0
for i in range(len(bkar)):
    if strong(bkar[i]) == True:
        arr2.append(bkar[i])
        cnt += 1

print(cnt)
for i in range(len(arr2)):
    print(arr2[i])