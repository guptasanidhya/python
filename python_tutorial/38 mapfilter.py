# number=["1","2","3"]
# number=list(map(int,number))
# print(number)
#################################################
# def sq(a):
#     return a*a
# num=["1","2","3"]
# nume=list(map(int,num))
# square=list(map(sq,nume))
# print(square)

# num=[1,2,3,4,5,6,7,8,9]
# square=list(map(lambda x: x*x,num))
# print(square)
#################################################
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
# num=[square,cube]
# for i in range (5):
#     val=list(map(lambda x:x(i),num))
#     print(val)
#
###################FILTER#############################
# list_n=[1,2,3,4,5,6,7,8]
# def grt_5(num):
#     return num>5
#
# list1=list(filter(grt_5,list_n))
# print(list1)

###############REDUCE#############################
from functools import reduce
list_n=[1,2,3,4,5,6,7,8]
num=reduce(lambda x,y:x+y , list_n)
print(num)