import random
print("welcome to the program")
print("Guess the correct number")
a= int(input("enter the lower range a="))
b= int(input("enter the higher range b="))
num= int(input("enter the number"))
i=random.randint(a,b)
count=1
while (1):
    if(num>i):
        b=num
        print("number is greater than the correct value now enter value between ",a ,"and",b)
        num = int(input("enter the  new number again"))
        count=count+1
        continue
    elif(num<i):
        a=num
        print("number is lesser than the correct value now enter value between ", a, "and", b)
        num = int(input("enter the  new number again"))
        count=count+1
        continue
    else:
        print("you guessed the correct number.\n","number of trials=",count)
        break





# while (num>i):
#     b=num
#     print("number is greater tha the correct value now enter value between ",a ,"and",b)
#     num = int(input("enter the  new number again"))
#     continue
# while(num>i):
#    print("no. is greater than correct number")
#    num = int(input("enter the new number "))
#    if(b>0):
#         b=b/2
#         continue
# else:
#     print("no. is less thn half")
