holder = []
temporary = map(str, input().split())
for i in temporary:
    if len(i) >= 3:
        holder.append(i)
print(*holder)