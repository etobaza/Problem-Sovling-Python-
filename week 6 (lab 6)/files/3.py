import os

path = input()
if os.path.exists(path):
    print("File:", os.path.basename(path))
    print("Directories/files:", os.listdir(path))
else: 
    print("Error")