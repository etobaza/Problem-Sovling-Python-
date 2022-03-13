import os

path = input()
try:
    os.remove(path)
except:
    print("Error!")