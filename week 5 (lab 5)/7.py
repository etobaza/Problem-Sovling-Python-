import re

def camel(s):
    return s.group(0)[1].upper()

a = input()
x = re.sub("_[a-z]", camel, a)
print(x)  