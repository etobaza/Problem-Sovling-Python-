s = input()

if s == s[slice(None, None, -1)]:
    print("Palindrome")
else:
    print("Not palindrome")
