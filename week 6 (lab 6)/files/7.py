first = open('first.txt', 'r')
second = open('second.txt', 'r')

for i in first:
    second.write(i)