import os

maindir = os.listdir() 
for i in maindir:
    if os.path.isdir(i): #List only directories
        print(i) 

for i in maindir: #List files and directories
    print(i)

path = input("Enter path: ") 
spec_dir = os.listdir(path)
for i in spec_dir: #List files in a specified path
    print(i)
