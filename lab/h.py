word = str(input())
let = str(input())
first = word.find(let)

for i in range (first, len(word)):
    if word[i] == let:
        last = i
if last != first:
    print(first, last)
else: 
    print(first)