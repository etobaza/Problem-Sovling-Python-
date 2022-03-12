s = input()
lower = 0
upper = 0
for i in s:
    if ord(i) >= 97 or ord(i) <= 122:
        lower += 1
    elif ord(i) >= 65 or ord(i) <= 90:
        upper += 1
print("Amount of lower case:", lower, "\n" "Amount of upper case:", upper)