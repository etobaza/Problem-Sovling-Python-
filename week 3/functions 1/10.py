def unique(l):
    return list(dict.fromkeys(l))

s = input().split()
print(*unique(s))