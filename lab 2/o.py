
def toArray(s):   #разделяет строку на 3 секции, и возвращает массив из трех символов
    temp = ""
    arr = []
    for i in range(0, len(s), 3):
        temp = s[i] + s[i+1] + s[i+2]
        arr.append(temp)
        temp = ""
    return arr

def toNum(s): #возвращает числа вместо символов
    ONE = 1
    TWO = 2
    THR = 3
    FOU = 4
    FIV = 5
    SIX = 6
    SEV = 7
    EIG = 8
    NIN = 9
    ZER = 0

    if s == "ONE":
        return 1
    if s == "TWO":
        return 2
    if s == "THR":
        return 3
    if s == "FOU":
        return 4
    if s == "FIV":
        return 5
    if s == "SIX":
        return 6
    if s == "SEV":
        return 7
    if s == "EIG":
        return 8
    if s == "NIN":
        return 9
    if s == "ZER":
        return 0

def numArray(arr): #принимает массив из строк длиной в 3 символа и возвращает массив из чисел
    temp = []
    for i in range(len(arr)):
       temp.append(toNum(arr[i]) )
    return temp


def uniteNum(arr): #соеденяет массив из чисел в одно число
    temp = 0
    length = len(arr)
    temp2 = 10**(length - 1)
    for i in range(length):
        temp += arr[i]*temp2
        temp2 = temp2//10
    return temp

s = input()
sep_string = s.split("+")

def pfn_to_final(n): #превратить массив из символов в массив чисел
    arr = []
    while n>0:
        arr.append(n%10)
        n=n//10
    return arr

def numToStr(arr): #возвращает cимволы вместо чисел
    s = ""
    for i in range(len(arr)):
        if arr[i] == 1:
            s = "ONE"+s
        if arr[i] == 2:
            s = "TWO"+s
        if arr[i] == 3:
            s = "THR"+s
        if arr[i] == 4:
            s = "FOU"+s
        if arr[i] == 5:
            s = "FIV"+s
        if arr[i] == 6:
            s = "SIX"+s
        if arr[i] == 7:
            s = "SEV"+s
        if arr[i] == 8:
            s = "EIG"+s
        if arr[i] == 9:
            s = "NIN"+s
        if arr[i] == 0:
            s = "ZER"+s
    return s

sep_chars = toArray(sep_string[0])
arr_of_ints = numArray(sep_chars)
normal_num1 = uniteNum(arr_of_ints)

sep_chars = toArray(sep_string[1])
arr_of_ints = numArray(sep_chars)
normal_num2 = uniteNum(arr_of_ints)

pre_final_num = normal_num1 + normal_num2
n1plusn2 = pfn_to_final(pre_final_num) 

print(numToStr(n1plusn2))
