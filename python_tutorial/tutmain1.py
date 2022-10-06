def add(x,y):
    return x+y

def function_name(str):
    print(f"this is my function {str}")
print(__name__)
if __name__ == '__main__':

    o=add(5,6)
    print(o)
    function_name("hello")
