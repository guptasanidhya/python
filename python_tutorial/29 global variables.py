x=31
def harry():
    x=25
    def rohan():
        global x # ye global keyword sab jagh se bahar jaake ek global x=30 create kardega aur pehle se hi koi value h to use replace
        x=30
    print("before calling rohan()",x)
    rohan()
    print("after calling rohan()",x)
harry()

print(x)
# l=5
# def fun():
#     global l #ye global keyword permisiion dega ki local k andr global use karlo
#     l=l+45
#     print(l)
# fun()
# print(l)