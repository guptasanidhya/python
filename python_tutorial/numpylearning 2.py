"""import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
"""

"""
import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10
"""

# range(N): [0, 1, 2, .... N-1]
# for x in range(N): loop x = 0, x = 1, ..., x = N-1
# for _ in range(N): loop N times
# input().split(): Split input by spaces and prepare list (fr ex 1 2 3 becomes ['1', '2', '3'])
# input().split() for _ in range(N): Read n lines and prepare n lists
# [input().split() for _ in range(N)]: Prepare a list from n lines input containing N times where each item itself is list of strings
# numpy.array([input().split() for _ in range(N)],int): Prepare 2d array from n lines of input with each item of type int
# A = numpy.array([input().split() for _ in range(N)],int): Assign the result to A
#sample input
# 2 2# types of length inputs
# 1 2
# 3 4

import numpy
ls=input().split()# returns ['2','2']
for i in range(len(ls)):#len=2
     ls[i] = int(ls[i])#changing strings to int


arr=[]

for i in range(ls[0]):#ls[0]=2
    extra=numpy.array(input().split(),int)#[1,2][3,4]
    arr.append(extra)
arr = numpy.array(arr)

print(numpy.prod(numpy.sum(arr , axis = 0)))
