# a=5
# b=5
# c=sum((a)) #built-in function
# print(c)
def function1():
    print("hello! your are in function 1")

function1()

def function2(a,b):
    """This is a function for average of two numbers only"""
    average=(a+b)/2
    print("average of two numbers=",average)
    return average

d=function2(1,2)
print(d)
print(function2.__doc__)
