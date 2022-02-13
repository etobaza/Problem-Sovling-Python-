def solve(numheads, numlegs):
    templegs = 2*numheads 
    total_legs = numlegs - templegs
    return("Rabbits:", total_legs // 2, "Chicken:", (35 - total_legs//2))

numheads = int(input())
numlegs = int(input())
print(*solve(numheads, numlegs))

