import re

a = input()
x = re.findall("[a-z]+_[a-z]+", a)
print(x)