# def func(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
#
#
#
# def execute(func):
#     func("this")
#
#
# execute(print)

def hello(func):
    def execute():
        print("executing function")
        func()
        print("executed")
    return execute

@hello
def hii():
    print("I am a good boy")

# hii=hello(hii)
hii()