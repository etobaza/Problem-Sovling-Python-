s = str(input())
for i in range(s):
    sum += ord(i)
if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")