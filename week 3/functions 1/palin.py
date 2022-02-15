def palindrome(s):
    if s[::-1] == s:
        return "Palindrome"
    else:
        return "Not Palindrome"
s = input()
print(palindrome(s)) 
