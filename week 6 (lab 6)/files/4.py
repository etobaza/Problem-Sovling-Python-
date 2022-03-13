import os

path = input()
open_file = open(path, 'r')
print("Amount of lines:", len(open_file.readlines())) 