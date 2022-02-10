n = int(input())
arr = []
student = {}
for i in range(n):
    name, cash = input().split()
    arr.append(name)

    if name in student:
        student[name] += int(cash)
    else:
        student[name] = int(cash)

lucky = student[max(student, key = student.get)]

fake_set = set(arr)
bkar = list(fake_set)
bkar.sort()

for i in range(len(student)):
    if lucky - student[bkar[i]] != 0:
        print(bkar[i], "has to receive", lucky - student[bkar[i]], "tenge")
    if lucky == student[bkar[i]]:
        print(bkar[i], "is lucky!")