import math

def is_prime(n):
        if n < 2:
            return False
        for j in range(2, int(math.sqrt(n))+1):
                if n % j == 0:
                    return False
        return True

list = input().split()

def checklist(l):
    prime_list = []
    for i in l:
        if is_prime(int(i)) == True:
            prime_list.append(int(i))
    return prime_list

print(checklist(list))