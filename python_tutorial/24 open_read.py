f=open("daily_data.txt","r")
# f=open("daily_data.txt","rt")
# f=open("daily_data.txt","rb")
"""read content in binary format binary string will display """
#content=f.read()
# print(f.readlines())
"""read the whole in 1 line with \n in a list """

# print(f.readline())
"""read one line with \n"""
# print(f.readline())
# print(f.readline())

# for line in f:
#     """reading f in line without \n because of end"""
#     print(line,end="")

# content=f.read()
# """print letter by letter with \n"""
# for line in content:
#     print(line)

# content=f.read(17)
# print("1",content)
# "reads the first content if available "
# content=f.read(3)
# print("2",content)
# "reads the second content if AVAILABLE"


# content=f.read(3) "read the first three character"
# print(content)
#content=f.read(3) "reads the next three character"
#print(content)
f.close()