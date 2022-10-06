
# a = input("What is your name")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f"Hello {a}")
# 1000 lines taking 1 hour
#
# Task - Write about 2 built in exception

# c = input("Enter your name")
# try:
#     print(a)
#
# except Exception as e:
#
#     if c =="sanidhya":
#         raise ValueError("sanidhya is blocked he is not allowed")
#
#
#     print("Exception handled")
"""KeyError: Raised when a mapping key is not found in the set of existing keys.
ValueError: Raised when a function receives an argument with the right type but an inappropriate value.
EOFError (End Of File Error): Raised when the input() function hits an end-of-file condition without reading any data.
ImportError: Raised when the import statement has trouble trying to load a module.
NameError: Raised when a local or global name is not found.
ZeroDivisionError: Raised when the second argument of a division is zero."""

# index error
# lst = [1, 2, 3, 4, 4, 6]
# for i in range(0, len(lst)):
#         if lst[i] == 4:
#             lst.pop(i)

#key error

"""
d={"hii":"hello","sanidhya":"gupta"}
for key in d.keys():
    if key!="sanidhya":
     print(d["hii"])
    else:
        raise KeyError

"""
