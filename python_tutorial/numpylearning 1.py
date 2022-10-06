import numpy
numpy.set_printoptions(legacy='1.13')#gives space after decimal point
#my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
my_array = numpy.array(input().split(), float)
#split the input into list and change the variable strings to float
print(my_array)
print(numpy.floor(my_array))#returns float value
print(numpy.ceil(my_array))#returns next largest  float-integer value
print(numpy.rint(my_array))# return the nearest float-integer value


