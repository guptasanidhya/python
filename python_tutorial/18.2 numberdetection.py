import random
print("welcome to the program")
print("Guess the correct number")
a=random.randint(0,0)
b=random.randint(100,100)
num= int(input("enter the number you guessed  between 0 to 100\n"))
i=random.randint(0,100)
count=1
while (count<=6):
    print("number of trials done ",count)
    print("No. of trials left",6-count)
    if(num==i):
        print("you won.You guessed the correct number.\n","number of trials=",count)
        break
    elif(count==6):
        print("no trials left")
        print("game over")
        print("Correct no.was",i)
        break
    elif(num<i):
        a=num
        print("number is lesser than the correct value now enter value between ", a, "and", b)
        num = int(input("enter the  new number again"))
        count=count+1
        continue
    elif(num>i):
        b=num
        print("number is greater than the correct value now enter value between ",a ,"and",b)
        num = int(input("enter the  new number again"))
        count=count+1
        continue