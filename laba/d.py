n = int(input())

if n%2 != 0:
    for i in range(n):
        for j in range(n-i-1):
            print(".", end = "")

        for k in range(i+1):
            print("#", end = '')
        print()

if n%2 == 0:
    for i in range(n):

        for k in range(i+1):
            print("#", end = '')

        for j in range(n-i-1):
            print(".", end = "")

        print()