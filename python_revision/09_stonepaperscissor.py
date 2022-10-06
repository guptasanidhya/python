import random
import sys

while(True):
    ls=["st","p","s"]
    object=random.choice(ls)
    print("Enter your Choice\n1.st for Stone\n2.p for Paper\n3.s for Scissor")
    user=input("enter:")

    if(user=="st"):
        if(user==object):
            print("its a tie")
        elif(object=="p"):
            print("computer wins ")
        elif(object=="s"):
            print("user wins")

    elif(user=="p"):
        if(user==object):
            print("its a tie")
        elif(object=="s"):
            print("computer wins ")
        elif(object=="st"):
            print("user wins")

    elif(user=="s"):
        if(user==object):
            print("its a tie")
        elif(object=="st"):
            print("computer wins ")
        elif(object=="p"):
            print("user wins")
    else:
        print("invalid input")
        sys.exit()

    print("computer choice",object)
    print("user choice",user)
