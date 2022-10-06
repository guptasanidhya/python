def getdate():
    import datetime
    return datetime.datetime.now()


def rohan():
    option=int(input("Enter 1 for diet \n 2 for exercise\nenter the Option Number "))
    if option==1:
        f=open("rohan-diet.txt","a")
        f.write("[")
        f.write(str(getdate()))
        f.write("] ")
        diet=input("Enter the diet plan for today\n")
        f.write(diet)
        f.write("\n")
        print("Entry done")
        f.close()
    elif option==2:
        f=open("rohan-exercise.txt","a")
        f.write("[")
        f.write(str(getdate()))
        f.write("] ")
        exercise=input("Enter the exercise \n")
        f.write(exercise)
        f.write("\n")
        print("Entry done")
        f.close()
    else:
        print("You hit the wrong button please re-enter the number")
        rohan()



def harry():
    option=int(input("enter 1 for diet \n  2 for exercise\nenter the Option Number "))
    if option==1:
        f=open("harry-diet.txt","a")
        f.write("[")
        f.write(str(getdate()))
        f.write("] ")
        diet=input("Enter the diet plan for today\n")
        f.write(diet)
        f.write("\n")
        print("entry done")
        f.close()
    elif option==2:
        f=open("harry-exercise.txt","a")
        f.write("[")
        f.write(str(getdate()))
        f.write("] ")
        exercise=input("Enter the exercise \n")
        f.write(exercise)
        f.write("\n")
        print("Entry done")
        f.close()
    else:
        print("You hit the wrong button please re-enter the number")
        harry()



def hammad():
        option = int(input("Enter 1 for diet \n 2 for exercise\nenter the Option Number "))
        if option == 1:
            f = open("hammad-diet.txt", "a")
            f.write("[")
            f.write(str(getdate()))
            f.write("] ")
            diet = input("Enter the diet plan for today\n")
            f.write(diet)
            f.write("\n")
            print("Entry done")
            f.close()
        elif option == 2:
            f = open("hammad-exercise.txt", "a")
            f.write("[")
            f.write(str(getdate()))
            f.write("] ")
            exercise = input("Enter the exercise \n")
            f.write(exercise)
            f.write("\n")
            print("Entry done")
            f.close()
        else:
            print("You hit the wrong button please re-enter the number")
            hammad()
print("Welcome to health care system")
while 1:
    name=input("Name of player for which you want to enter data\n Name-")
    if name=="rohan":
        rohan()
    elif name=="harry":
        harry()
    elif name=="hammad":
        hammad()
    else:
        print("Name doesn't exist in system\n Please re-enter the name ")