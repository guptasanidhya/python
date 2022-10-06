def getdate():
    import datetime
    return datetime.datetime.now()


def rohan():
    option=int(input("Enter 1 for diet \n 2 for exercise\nenter the Option Number "))
    if option==1:
        f=open("rohan-diet.txt","a")
        # f.write("[")

        # f.write(str(getdate()))
        # f.write("] ")
        diet=input("Enter the diet plan for today\n")
        f.write(str([str(getdate())])+" "+diet+"\n")
        # f.write(diet)
        # f.write("\n")
        print("Entry done")
        f.close()
    elif option==2:
        f=open("rohan-exercise.txt","a")
        # f.write("[")
        # f.write(str(getdate()))
        # f.write("] ")
        exercise=input("Enter the exercise \n")
        f.write(str([str(getdate())]) + " " + exercise + "\n")
        # f.write(exercise)
        # f.write("\n")
        print("Entry done")
        f.close()
    else:
        print("You hit the wrong button please re-enter the number")
        rohan()


def rohan_retrival():
    number=int(input("want to retrive data of diet or exercise.\n press 1 for diet 2 \n press 2 for exercise\n Enter the number-"))
    if number==1:
        with open("rohan-diet.txt") as f:
            get=f.readline()
            while get:
                print(get)
                get = f.readline()

    elif number==2:
        with open("rohan-exercise.txt") as f:
            get=f.readline()
            while get:
                print(get)
                get = f.readline()




def harry():
    option=int(input("enter 1 for diet \n  2 for exercise\nenter the Option Number "))
    if option==1:
        f=open("harry-diet.txt","a")
        # f.write("[")
        # f.write(str(getdate()))
        # f.write("] ")
        diet=input("Enter the diet plan for today\n")
        f.write(str([str(getdate())]) + " " + diet + "\n")
        # f.write(diet)
        # f.write("\n")
        print("entry done")
        f.close()
    elif option==2:
        f=open("harry-exercise.txt","a")
        # f.write("[")
        # f.write(str(getdate()))
        # f.write("] ")
        exercise=input("Enter the exercise \n")
        f.write(str([str(getdate())]) + " " + exercise + "\n")
        # f.write(exercise)
        # f.write("\n")
        print("Entry done")
        f.close()
    else:
        print("You hit the wrong button please re-enter the number")
        harry()

def harry_retrival():
    number=int(input("want to retrive data of diet or exercise.\n press 1 for diet 2 \n press 2 for exercise\n Enter the number-"))
    if number==1:
        with open("harry-diet.txt") as f:
            get=f.readline()
            while get:
                print(get)
                get = f.readline()

    elif number==2:
        with open("harry-exercise.txt") as f:
            get=f.readline()
            while get:
                print(get)
                get = f.readline()


def hammad():
        option = int(input("Enter 1 for diet \n 2 for exercise\nenter the Option Number "))
        if option == 1:
            f = open("hammad-diet.txt", "a")
            # f.write("[")
            # f.write(str(getdate()))
            # f.write("] ")
            diet = input("Enter the diet plan for today\n")
            f.write(str([str(getdate())]) + " " + diet + "\n")
            # f.write(diet)
            # f.write("\n")
            print("Entry done")
            f.close()
        elif option == 2:
            f = open("hammad-exercise.txt", "a")
            # f.write("[")
            # f.write(str(getdate()))
            # f.write("] ")
            exercise = input("Enter the exercise \n")
            f.write(str([str(getdate())]) + " " + exercise + "\n")
            # f.write(exercise)
            # f.write("\n")
            print("Entry done")
            f.close()
        else:
            print("You hit the wrong button please re-enter the number")
            hammad()

def hammad_retrival():
    number=int(input("want to retrive data of diet or exercise.\n press 1 for diet 2 \n press 2 for exercise\n Enter the number-"))
    if number==1:
        with open("hammad-diet.txt") as f:
            get=f.readline()
            while get:
                print(get)
                get = f.readline()

    elif number==2:
        with open("hammad-exercise.txt") as f:
            get=f.readline()
            while get:
                print(get)
                get = f.readline()
print("Welcome to health care system")
while 1:
 take=int(input("want to enter data or want to retrive data \n press 1 for enter \n press 2 for retriving data. \n Enter the number- "))
 if take==1:
    name=input("Name of player for which you want to enter data\n Name-")
    if name=="rohan":
        rohan()
    elif name=="harry":
        harry()
    elif name=="hammad":
        hammad()
    else:
        print("Name doesn't exist in system\n Please re-enter the name ")

 elif take==2:
     name = input("Name of player of which you want to retrive data\n Name-")
     if name == "rohan":
         rohan_retrival()
     elif name == "harry":
         harry_retrival()
     elif name == "hammad":
         hammad_retrival()