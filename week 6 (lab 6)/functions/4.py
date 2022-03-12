import time

ogtime = int(input())
mlsec = int(input())

time.sleep(mlsec/1000)
sqrt = "pow(ogtime, 1/2)"
print("Square root of", ogtime, "after", mlsec, "mileseconds is", eval(sqrt))