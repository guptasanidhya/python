# print("welcome to star system")
# n=int(input("enter the no of stars"))
#
# for n in range(0,n):
#         print("*"*(n+1))
print("Welcome to star system")
print("How many rows you want to print")
try:
        row=(int(input("enter the no. of rows")))
        value=bool(int(input("enter the value 0 or 1 ")))
        print("value=",value)
        if value==True:
                for i in range (0,row+1):
                        print("*"*(i))
        elif value==False:
                for i in range (row,0,-1):
                        print("*"*(i))
except Exception as e:
        print("wrong entry")

