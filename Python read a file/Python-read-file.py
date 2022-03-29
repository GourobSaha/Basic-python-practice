# Read a file
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

# Write a file
text = "Yooooooooo\nThis is some text\nHave a good one!\n"

with open('test.txt','w') as file:
    file.write(text)


# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src,dst


# Move a file
import os

source = "C:\\Users\\User\\Desktop\\source.txt"
destination = "C:\\Users\\User\\Desktop\\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")


# Remove a file or a directory
import os
import shutil

path = "test.txt"

try:
    os.remove(path)        #delete a file
    #os.rmdir(path)        #delete an empty directory
    #shutil.rmtree(path)   #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")