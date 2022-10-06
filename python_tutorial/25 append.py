
# f=open("daily_data.txt","r")
#f.write("\ndate-15/march/2021\n I woke up at 5 AM")
"""will remove all the things and start a new session"""
# f=open("daily_data.txt","a")
# """will append the new line"""
# a=f.write("\ndate-3/april/2021\n I woke up at 5 AM")
# print(a)
"""will print no. of characters in the file"""
# f.close()
f=open("daily_data.txt","r+")
# r+ will do both read and write function
print(f.read())
# f.write("\nDate-16/march/2021\nI woke up at 5 AM")
# f.write("\nDate-1/april/2021\nI woke up at 9 AM")
# f.write("\nDate-2/april/2021\n I woke up at 5 AM")
f.close()
