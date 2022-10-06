def function(normal,*args,**kwargs):
    for item in args:
        print(normal,item)
    for key,value in kwargs.items():
        print(f"{key} is the starter {value}")

args=["Sanidhya","Mohini","nitin"]
kw={"Sanidhya":"player","mohini":"dancer","nitin":"coder"}
normal="This is a normal argument"
function(normal,*args,**kw)

# d1={"Sanidhya":"Gupta"}
list=["Sanidhya"]
c=input("enter the new key")
# d=input("enter the new value")
# d1[c]=d
# print(d1)
args.append(c)
print(args)