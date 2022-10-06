apple=int(input("enter the apple sanidhya got:"))
mn=int(input("Enter the minimum students:"))
mx=int(input("enter the maximum students:"))
if mn==mx:
    print(f"this is not a range. Both values are equal")
else:
    for student in range(mn,mx):
        if apple%student==0:
            apples=int(apple/student)
            print(f" {student} students will get {apples} apple each ")
        else:
            print(f"student will not get anything because {apple} apples is not divisible by {student} students equally")
