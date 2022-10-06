import os
"""OS module provides our code with a direct connection to the operating system. 
We can use its different functions to interact and do activities on our operating system. 
For example, if we want to create such software that needs to store or access files from a directory or folder,
 we can use the OS module to perform the task for us. To use OS Module in Python, we have to import it."""
print(dir(os))
print(os.getcwd())

# os.chdir("C://Users//hp")
# print(os.getcwd())
# f=open("sanidhya.txt")
# print(os.listdir("C://"))
# os.makedirs("this/that")
# os.rename("sanidhya.txt","Sanidhya.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C://","Sanidhya.txt"))
print(os.path.exists("C://Users"))
print(os.path.isfile("Sanidhya.txt"))
print(os.path.isdir("C://Users"))

"""
# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "GeeksforGeeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)

# Directory
directory = "Geeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
"""