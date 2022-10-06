class A:
    classvar1="I am in class A"

    def __init__(self):
        self.classvar1="i am in instance of class A"
        self.special="I am Special"

class B(A):
    classvar="I am in class b"
    def __init__(self):

        self.classvar1="i am in instance pf class B"
        super().__init__()
        self.var="i am Sanidhya"
a=A()
b=B()

print(b.classvar1)
print(b.var)
print(b.special)
# print(b.classvar1)