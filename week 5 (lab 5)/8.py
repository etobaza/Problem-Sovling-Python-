import re

a = input()
x = re.split("(?=[A-Z])", a)
print(x)