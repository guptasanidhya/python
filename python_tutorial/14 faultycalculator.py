#45*3=555,56+9=77,56/6=4
print("welcome to calculator")
print("Enter Two numbers")
a=int(input("input a ="))
b=int(input("input b ="))
print("Which operation do you want to perform")
op =input()
if op=="+":
    if (a==56 and b==9) or (a==9 and b==56):
        print("sum=77")
    else:
        sum=a+b
        print("sum = ",sum)
elif op=="*":
    if (a==43 and b==3) or (a==3 and b==43):
        print("mul=555")
    else:
        mul=a*b
        print("mul = ",mul)
elif op=="/":
    if (a==56 and b==6):
        print("div=4")
    else:
        div=a/b
        print("div = ",div)
elif op=="-":
    sub=a-b
    print("subtract=",sub)
