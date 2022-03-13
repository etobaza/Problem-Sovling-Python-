import os


path = input("Enter path: ") 
if os.path.isfile(path): #Check file existence
    print("File exists!")
else:
    print("File non-existent or it's a folder.")

if os.access(path, os.R_OK): #Check if file can be read
    print("Can be read!")
else:
    print("Can't be read.")

if os.access(path, os.W_OK):
    print("Can be written!") #Check if file can be written
else:
    print("Can't be written.")

if os.access(path, os.X_OK): 
    print("Executable!") #Check if file can be written
else:
    print("Non executable.")