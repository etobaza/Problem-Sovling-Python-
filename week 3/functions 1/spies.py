def spy_game(nums):
    flag = True
    zeros = 0
    seven = 0
    for i in range(len(nums)):
        if nums[i] == "0":
            zeros+=1
            zero_pos = int(i)
        if nums[i] == "7":
            seven+=1
            seven_pos = int(i)
        if zeros == 2 and seven == 1 and zero_pos<seven_pos:
            flag = True
        else:
            flag = False
    return flag

s = input().split()
print(spy_game(s))