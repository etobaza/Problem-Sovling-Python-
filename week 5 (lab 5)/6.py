import re

a = input()
x = re.sub("\s|,|\.", ":", a)
print(x)