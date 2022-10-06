# i=0
# while(1):
#     if(i<5):
#         i=i+1
#         continue
#     print(i)
#     i=i+1
#     if(i==44):
#         break
#
print("Welcome to program")
num=int(input("Enter the Number\n"))
while(True):
    if(num<100):
        print(num)
        num = int(input("Number is small. Enter the Number again\n"))
        continue
    else:
        print("number is greater")
        break