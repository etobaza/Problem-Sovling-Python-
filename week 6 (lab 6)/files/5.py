list = ['Free', 'Ukraine']
file_open = open('listfile_5.txt', 'w')
for i in list:
    file_open.write(i)
    file_open.write("\n")
print("Complete!")
  