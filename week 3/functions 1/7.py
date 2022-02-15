def has_33(nums):
    flag = True
    for i in range(len(nums)):
        if nums[i] == "3" and nums[i-1] == "3":
                flag = True
        else:
                flag = False
    return flag

s = input().split()
print(has_33(s))