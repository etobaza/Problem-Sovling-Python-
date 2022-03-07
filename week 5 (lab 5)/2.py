import re

a = input()
x = re.search("ab{2,3}", a)
print(x)