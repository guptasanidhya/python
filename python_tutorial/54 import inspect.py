"""isclass(): The isclass() method returns True if that object is a class or false otherwise.
 When it is combined with the getmembers() functions it shows the class and its type.
  It is used to inspect live classes."""
# import required modules
"""import inspect

# create class
class A(object):
	pass

# use isclass()
print(inspect.isclass(A))
"""


"""ismodule(): This returns true if the given argument is an imported module."""
"""# import required modules 
import inspect
import numpy

# use ismodule()
print(inspect.ismodule(numpy))
"""

"""isfunction(): This method returns true if the given argument is an inbuilt function name."""
"""
# import required modules
import inspect

# explicit function
def fun(a):
	return 2*a

# use isfunction()
print(inspect.isfunction(fun))

"""

"""ismethod(): This method is used to check if the argument passed is the name of a method or not."""
# import required modules
"""import inspect
import collections

# use ismethod()
print(inspect.ismethod(collections.Counter))
"""

"""getclasstree(): The getclasstree() method will help in getting and inspecting class hierarchy. 
It returns a tuple of that class and that of its preceding base classes. 
That combined with the getmro() method which returns the base classes helps
 in understanding the class hierarchy."""
"""# import required module
import inspect

# create classes
class A(object):
	pass

class B(A):
	pass

class C(B):
	pass

# not nested
print(inspect.getmro(C)) """

"""# import required module
import inspect

# create classes
class A(object):
	pass

class B(A):
	pass

class C(B):
	pass

# nested list of tuples
for i in (inspect.getclasstree(inspect.getmro(C))):
	print(i)
"""

# getmembers(): This method returns the member functions
# present in the module passed as an argument of this method.
# import required module
"""import inspect
import math

# shows the member functions
# of any module or object
print(inspect.getmembers(math))"""

# signature(): The signature() method helps the user in
# understanding the attributes which are to be passed on to a function.
# import required modules
"""import inspect
import collections

# use signature()
print(inspect.signature(collections.Counter))
"""
# stack(): This method helps in examining the interpreter
# or the order in which functions were called.
# import required module
"""import inspect

# define explicit function
def Fibonacci(n):
	if n < 0:
		return 0

	elif n == 0:
		return 0

	elif n == 1:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)


# Driver Program
(Fibonacci(12))

# inpsecting interpreter stack
print(inspect.stack())"""

# getsource(): This method returns the source code of a module,
# class, method, or a function passes as an argument of getsource() method.
# import required modules
"""import inspect

def fun(a,b):
	# product of
	# two numbers
	return a*b

# use getsource()
print(inspect.getsource(fun))
"""
# getmodule(): This method returns the module name of a particular object
# pass as an argument in this method.
# import required modules
"""import inspect
import collections

# use getmodule()
print(inspect.getmodule(collections))"""
# getdoc(): The getdoc() method returns the documentation
# of the argument in this method as a string.
# import required modules
"""import inspect
from tkinter import *

# create object
root = Tk()

# use getdoc()
print(inspect.getdoc(root))"""






