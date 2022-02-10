n = int(input())
arr = []  #список для хранения имен студентов
student = {} #словарь для хранения студентов
for i in range(n):
    name, cash = input().split()
    arr.append(name)

    if name in student: #добавление студентов в словарь или суммирование денег существуюших студентов
        student[name] += int(cash) 
    else:
        student[name] = int(cash)

lucky = student[max(student, key = student.get)] #переменная lucky, хранится самый богатенький буржуй

fake_set = set(arr) #избавляюсь от повторений с списке имен
bkar = list(fake_set) #back_to_array, возвращаю set обратно в список
bkar.sort() #сортировка порядка имен в списке

for i in range(len(student)): #вывод 
    if lucky - student[bkar[i]] != 0:
        print(bkar[i], "has to receive", lucky - student[bkar[i]], "tenge")
    if lucky == student[bkar[i]]:
        print(bkar[i], "is lucky!")